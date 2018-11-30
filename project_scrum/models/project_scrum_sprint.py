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

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     #When adding/removing tasks or changing start/end dates to a sprint, update the start/end dates on the tasks to match sprint for forecasting
     @api.onchange('project_tasks', 'start_date', 'end_date')
     def on_change_project_tasks(self):
         for record in self.project_tasks:
             if record.date_start != self.start_date:
                 record.write({'date_start': self.start_date})
             if record.date_end != self.end_date:
                 record.write({'date_end': self.end_date})
             if record.date_end != self.end_date:
                 record.write({'date_deadline': self.end_date})
             if record.forecasts:
                 # Get EmployeeID from the user_id
                 for each_forecast in record.forecasts:
                     each_forecast.write({'start_date': record.date_start, 'end_date': record.date_end})


     @api.multi
     def close_and_create_sprint(self):
         sprintid = self.id + 1
         sprint_start = date.today()
         sprint_end = date.today() + relativedelta(days=+14)
         new_sprint = self.env['project.scrum_sprint'].create({'name': "Sprint - " + str(sprintid), 'start_date': sprint_start, 'end_date': sprint_end, 'projects': [6, 0, self.projects.ids]})
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

     def close_sprint(self):
         if self.status != 'closed':
             for record in self.project_tasks:
                 if record.stage_id.is_closed == False:
                     record.sprint_id = False
             self.status = 'closed'
