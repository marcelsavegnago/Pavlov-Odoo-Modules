from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _order = 'priority desc, date_start, date_end, sequence, date_start, id desc'

    forecasts = fields.One2many('project.forecast',
                                'task_id',
                                string="Forecasts",
                                help="List of Forecasts related to the Task.")
    allow_auto_forecast = fields.Boolean(string="Allow Auto Forecasts",
                                         related='project_id.allow_auto_forecast',
                                         help="Enables the ability for forecasts to be auto created on the Task. Related to the Project 'Allow Auto Forecasts' setting. Requires the Task to be assigned, start/end dates and planned hours.")

    # UPDATE OR CREATE FORECAST AUTOMATICALLY IF ALL REQUIRED VALUES ARE MET
    @api.onchange('date_start', 'date_end', 'sprint_id', 'planned_hours')
    def on_change_task_forecast(self):
        # Only perform this action if the project has 'Allow Auto Forecasts' enabled AND all the forecast required fields are filled in
        if self.allow_auto_forecast and self.date_start and self.date_end and self.planned_hours and self.user_id:
            # If Task already has Forecasts then update them
            if self.forecasts:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then each forecast record can be updated
                if employee_id.id:
                    for record in self.forecasts: # MAYBE NEED and employee.id == employee_id (to only update forecasts related to the assigned user)
                        record.sudo().write({'start_date': self.date_start,
                                             'end_date': self.date_end,
                                             'sprint_id': self.sprint_id.id,
                                             'resource_hours': self.planned_hours,
                                             'employee_id': employee_id.id})

            # If no forecasts exist then create it
            else:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then a forecast record can be created...
                if employee_id.id:
                    self.env['project.forecast'].sudo().create({'sprint_id': self.sprint_id.id,
                                                                'employee_id': employee_id.id,
                                                                'project_id': self.project_id.id,
                                                                'resource_hours': self.planned_hours,
                                                                'task_id': self._origin.id,
                                                                'start_date': self.date_start,
                                                                'end_date': self.date_end})
