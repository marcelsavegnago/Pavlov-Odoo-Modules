from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# GLOBAL ENHANCEMENTS
    next_task_number = fields.Integer(string="Next Task Number", default="1", copy=False, help="Each Project can have it's own task numbers and get added to the Task Label.")
    project_status = fields.Many2one('project.status', string="Status", help="Project status options are global status, configured in the Configuration menu.")
    department = fields.Many2one('hr.department', string="Department", help="The department that this Project is related to.")
    old_start_date = fields.Date(string='Old Start Date', help="Used by the Shift Dates function. When the Projects start date changes, the old date is populated in this field then is used when the 'Shift Dates' button is pushed.")
    allow_auto_forecast = fields.Boolean(string="Allow Auto Forecasts", help="Enables the ability for forecasts to be auto created on Project Tasks. Requires the Task to be assigned, start/end dates and planned hours.")
    project_type = fields.Many2one('project.type', string="Project Type", help="The type of Project", required=True)

# NEW COMPUTE FIELDS
    progress = fields.Float(string="Progress", compute="_compute_project_progress", store=True, help="Percentage of Completed Tasks vs Incomplete Tasks.")
    total_planned_hours = fields.Float(string="Total Planned Hours", compute='_compute_total_planned_hours', store=True, help="Total planned hours from all related Project Tasks.")
    total_effective_hours = fields.Float(string="Total Spent Hours", compute='_compute_total_effective_hours', store=True, help="Total spent hours from all related Project Tasks.")
    total_remaining_hours = fields.Float(string="Total Remaining Hours", compute='_compute_total_remaining_hours', store=True, help="Total remaining hours from all related Project Tasks.")

    # COMPUTE PROJECT PROGRESS
    @api.depends('task_ids.stage_id')
    def _compute_project_progress(self):
        total_tasks_count = 0.0
        closed_tasks_count = 0.0
        for record in self:
            for task_record in record.task_ids:
                total_tasks_count += 1
                if (task_record.stage_id.is_closed == True):
                    closed_tasks_count += 1
            if (total_tasks_count > 0):
                record.progress = (closed_tasks_count / total_tasks_count) * 100
            else:
                record.progress = 0.0

    # COMPUTE PLANNED HOURS
    @api.depends('task_ids.planned_hours')
    def _compute_total_planned_hours(self):
        for record in self:
            if record.allow_timesheets and record.task_ids:
                tasks = record.env['project.task'].search([('project_id', '=', record.id)])
                planned_total = 0.0
                for task_record in tasks:
                    planned_total += task_record.planned_hours
                record.update({'total_planned_hours': planned_total})

    # COMPUTE EFFECTIVE HOURS
    @api.depends('task_ids.effective_hours')
    def _compute_total_effective_hours(self):
        for record in self:
            if record.allow_timesheets and record.task_ids:
                effective_total = 0.0
                timesheets = record.env['account.analytic.line'].search([('project_id', '=', record.id)])
                for timesheet_record in timesheets:
                    effective_total += timesheet_record.unit_amount
                record.update({'total_effective_hours': effective_total})

    # COMPUTE REMAINING HOURS
    @api.depends('total_planned_hours','total_effective_hours')
    def _compute_total_remaining_hours(self):
        for record in self:
            if record.allow_timesheets and record.task_ids:
                hours_planned_total = 0.0
                hours_effective_total = 0.0
                hours_remaining_total = 0.0
                tasks = record.env['project.task'].search([('project_id', '=', record.id)])
                timesheets = record.env['account.analytic.line'].search([('project_id', '=', record.id)])

                for task_record in tasks:
                    hours_planned_total += task_record.planned_hours

                for timesheet_record in timesheets:
                    hours_effective_total += timesheet_record.unit_amount

                hours_remaining_total = hours_planned_total - hours_effective_total
                record.update({'total_remaining_hours': hours_remaining_total })

    # UPDATE TASK NUMBER LABELS IF THE MAIN LABEL CHANGED
    @api.onchange('label_tasks')
    def on_change_label_tasks(self):
        if self._origin.label_tasks:
            old_label = self._origin.label_tasks
            new_label = self.label_tasks
            for record in self.task_ids:
                new_task_number = record.task_number
                new_task_number = new_task_number.replace(old_label, new_label)
                record.write({'task_number': new_task_number})

    # UPDATE ANALYTIC ACCOUNT IF PROJECT NAME CHANGES
    @api.onchange('name')
    def on_change_name(self):
        if self.analytic_account_id:
            # ONLY CHANGE IF THE ANALYTIC ACCOUNT SHARES THE SAME NAME AS THE PROJECT NAME (COMPANY MAY WANT TO LINK PROJECTS TO CUSTOMERS AND WE WOULDN'T WANT TO CHANGE THAT)
            if self._origin.name == self.analytic_account_id.name:
                for record in self.analytic_account_id:
                    record.write({'name': self.name})

    # SET OLD DATA VALUES WHEN CHANGED *USED FOR DATE SHIFTING
    @api.onchange('date_start')
    def on_change_dates(self):
        if self.old_start_date == False:
            self.old_start_date = self._origin.date_start
        if self.old_start_date == self.date_start:
            self.old_start_date = False

    # SHIFT TASK AND MILESTONE DATES
    def shift_dates(self):
        # ONLY RUN IS SHIFT DATES OPTION IS TRUE
        if self.shift_task_dates and (self.old_start_date != self.date_start):
            original_start_dt = fields.Datetime.from_string(self.old_start_date)
            new_start_dt = fields.Datetime.from_string(self.date_start)
            difference = relativedelta(new_start_dt, original_start_dt)
            years = difference.years
            months = difference.months
            days = difference.days

            # SHIFT TASK DATES
            for record in self.task_ids:
                if record.active and (record.stage_id.is_closed != True):
                    if record.date_start:
                        record.write({'date_start': (record.date_start + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_start': record.project_id.date_start})

                    if record.date_end:
                        record.write({'date_end': (record.date_end + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_end': record.project_id.date})

                    if record.date_end > record.project_id.date:
                        record.project_id.write({'date': record.date_end})

                    if record.date_deadline:
                        record.write({'date_deadline': (record.date_deadline + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_deadline': record.project_id.date})

            # SHIFT MILESTONE DATES
            if self.use_milestones:
                for record2 in self.milestones:
                    if record2.target_date:
                        record2.write({'target_date': (record2.target_date + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})

        self.old_start_date = False

# SCRUM
    sprints = fields.Many2many('project.scrum_sprint', relation='project_sprint_rel', column1='project_id', column2='sprint_id', string="Sprints", copy=False)
    use_scrum = fields.Boolean(string="Use Scrum", copy=True, context="{'default_use_scrum': use_scrum}")
    releases = fields.One2many('project.scrum_release', 'project_id', string="Releases", copy=False)

# MILESTONES
    milestones = fields.One2many('project.milestone', 'project_id', string="Milestones", copy=True)
    use_milestones = fields.Boolean(string="Use Milestones", copy=True)

# TEMPLATE
    is_template = fields.Boolean(string="Is Template", copy=False)
    shift_task_dates = fields.Boolean(string="Shift Task Dates?", default=True, help="If checked, when you change the start date of a project, the dates on the Tasks will shift the number of days you change the start date of the Project. If the Project start dates were originally empty, the Start/End dates on the tasks will be set to the Project Start/End Dates unless they were previously set on the Tasks.")

    # CREATE A PROJECT FROM A TEMPLATE AND OPEN THE NEWLY CREATED PROJECT
    def create_project_from_template(self):
        if " (TEMPLATE)" in self.name:
            new_name = self.name.replace(" (TEMPLATE)"," (COPY)")

        new_project = self.copy(default={'name': new_name, 'active': True, 'total_planned_hours': 0.0})
        new_project.next_task_number = self.next_task_number
        if new_project.subtask_project_id != new_project.id:
            new_project.subtask_project_id = new_project.id
        # Clear Email Alias if it was set in the Template
        if new_project.alias_name:
            new_project.alias_name = False

        # SINCE THE END DATE DOESN'T COPY OVER ON TASKS, POPULATE END DATES ON THE TASK
        for record in new_project.tasks:
            if record.date_start and record.date_end == False:
                record.write({'date_end': (record.date_start + relativedelta(days =+ 7))})

        # OPEN THE NEWLY CREATED PROJECT FORM
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.project',
            'target': 'current',
            'res_id': new_project.id,
            'type': 'ir.actions.act_window'
        }
        # FORCE PAGE REFRESH TO ALLOW FOR PROPER ONCHANGE EVENTS LIKE SHIFTING DATES
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    # ADD "(TEMPLATE)" TO THE NAME WHEN PROJECT IS MARKED AS A TEMPLATE
    @api.onchange('is_template')
    def on_change_is_template(self):
        # Add "(TEMPLATE)" to the Name if is_template == true
        if self.name:
            if self.is_template == True:
                if "(TEMPLATE)" not in self.name:
                    self.name = self.name + " (TEMPLATE)"
                if self.user_id:
                    self.user_id = False
                if self.partner_id:
                    self.partner_id = False
                if self.alias_name:
                    self.alias_name = False

            else:
                if " (TEMPLATE)" in self.name:
                    self.name = self.name.replace(" (TEMPLATE)","")
