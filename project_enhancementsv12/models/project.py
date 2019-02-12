from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# NEW COMPUTE FIELDS
    progress = fields.Float(string="Progress",
                            compute="_compute_project_progress",
                            store=True,
                            help="Percentage of Completed Tasks vs Incomplete Tasks.")
    total_planned_hours = fields.Float(string="Total Planned Hours",
                                       compute='_compute_total_planned_hours',
                                       store=True,
                                       help="Total planned hours from all related Project Tasks.")
    total_effective_hours = fields.Float(string="Total Spent Hours",
                                         compute='_compute_total_effective_hours',
                                         store=True,
                                         help="Total spent hours from all related Project Tasks.")
    total_remaining_hours = fields.Float(string="Total Remaining Hours",
                                         compute='_compute_total_remaining_hours',
                                         store=True,
                                         help="Total remaining hours from all related Project Tasks.")

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

    # UPDATE ANALYTIC ACCOUNT IF PROJECT NAME CHANGES
    @api.onchange('name')
    def on_change_name(self):
        if self.analytic_account_id:
            # ONLY CHANGE IF THE ANALYTIC ACCOUNT SHARES THE SAME NAME AS THE PROJECT NAME (COMPANY MAY WANT TO LINK PROJECTS TO CUSTOMERS AND WE WOULDN'T WANT TO CHANGE THAT)
            if self._origin.name == self.analytic_account_id.name:
                for record in self.analytic_account_id:
                    record.write({'name': self.name})
