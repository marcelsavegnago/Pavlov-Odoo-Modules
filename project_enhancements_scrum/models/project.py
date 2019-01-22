from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# SCRUM
    next_task_number = fields.Integer(string="Next Task Number",
                                      default="1",
                                      copy=False,
                                      help="Each Project can have it's own task numbers and get added to the Task Label.")
    allow_auto_forecast = fields.Boolean(string="Allow Auto Forecasts",
                                         help="Enables the ability for forecasts to be auto created on Project Tasks. Requires the Task to be assigned, start/end dates and planned hours.")
    sprints = fields.Many2many('project.scrum_sprint',
                               relation='project_sprint_rel',
                               column1='project_id',
                               column2='sprint_id',
                               string="Sprints",
                               copy=False)
    use_scrum = fields.Boolean(string="Use Scrum",
                               copy=True,
                               context="{'default_use_scrum': use_scrum}")
    releases = fields.One2many('project.scrum_release',
                               'project_id',
                               string="Releases",
                               copy=False)
    epics = fields.One2many('project.scrum_epic',
                            'project_id',
                            string="Epics",
                            copy=True)

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
