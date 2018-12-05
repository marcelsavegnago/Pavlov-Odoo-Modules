from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class ProjectSprint(models.Model):
     _name = 'project.scrum_sprint'

#General
     name = fields.Char(string="Sprint Name", required=True)
     goal = fields.Char(string="Sprint Goal")
     start_date = fields.Date(string="Start Date", required=True)
     end_date = fields.Date(string="End Date", required=True)
     percent_complete = fields.Integer(string="Percent Complete")
     status = fields.Selection([('planning', 'Planning'),('active', 'Active'),('review','Review'),('closed','Closed')], default="planning")

     project_tasks = fields.One2many('project.task', 'sprint_id', string="Project Tasks")
     scrum_teams = fields.Many2many('project.scrum_team', string="Scrum Teams")
     projects = fields.Many2many('project.project', relation='project_sprint_rel', column1='sprint_id', column2='project_id', string="Projects", required=True)
     forecasts = fields.One2many('project.forecast', 'sprint_id', string="Forecasts")

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
         ('check_start_date_lower_end_date', 'CHECK(end_date >= start_date)', 'Sprint End Date should be greater or equal to its Start Date'),
     ]

     # UPDATE OR CREATE FORECAST AUTOMATICALLY IF ALL REQUIRED VALUES ARE MET IF A TASK, START/END DATES CHANGE
     @api.onchange('project_tasks', 'start_date', 'end_date')
     def on_change_update_create_task_forecast(self):
         for record in self.project_tasks:
             if record.date_start != self.start_date:
                 record.write({'date_start': self.start_date})
             if record.date_end != self.end_date:
                 record.write({'date_end': self.end_date})
             if record.date_end != self.end_date:
                 record.write({'date_deadline': self.end_date})

             if record.date_start and record.date_end and record.planned_hours and record.user_id and record.allow_forecast:
                 if record.forecasts:
                     for forecast_record in record.forecasts:
                         employee_id = self.env['hr.employee'].search([('user_id', '=', record.user_id.id)])
                         if employee_id.id:
                              forecast_record.write({'start_date': self.start_date, 'end_date': self.end_date, 'resource_hours': record.planned_hours, 'employee_id': employee_id.id})
                 else:
                     employee_id = self.env['hr.employee'].search([('user_id', '=', record.user_id.id)])
                     if employee_id.id:
                         self.env['project.forecast'].create({'sprint_id': record.sprint_id.id, 'employee_id': employee_id.id, 'project_id': record.project_id.id, 'resource_hours': record.planned_hours, 'task_id': record.id, 'start_date': record.date_start, 'end_date': record.date_end})

     # CLOSE AND CREATE BUTTON
     @api.multi
     def close_and_create_sprint(self):
         sprintid = self.id + 1
         sprint_start = date.today()
         sprint_end = date.today() + relativedelta(days=+14)
         project_ids = []
         project_ids = self.projects.ids
         team_ids = []
         team_ids = self.scrum_teams.ids
         new_sprint = self.env['project.scrum_sprint'].create({'name': "Sprint - " + str(sprintid), 'start_date': sprint_start, 'end_date': sprint_end, 'projects': [(6,0,project_ids)], 'scrum_teams': [(6,0,team_ids)]})
         for record in self.project_tasks:
             if record.stage_id.is_closed == False:
                record.sprint_id = new_sprint
         self.status = 'closed'

         return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.scrum_sprint',
            'target': 'current',
            'res_id': new_sprint.id,
            'type': 'ir.actions.act_window'
         }

     # CLOSE BUTTON
     def close_sprint(self):
         if self.status != 'closed':
             for record in self.project_tasks:
                 if record.stage_id.is_closed == False:
                     record.sprint_id = False
             self.status = 'closed'
