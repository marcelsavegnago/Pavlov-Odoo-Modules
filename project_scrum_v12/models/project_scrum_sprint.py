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
             self.status = 'closed'
