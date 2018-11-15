from odoo import models, fields, api

#Main Bandwidth Change Records Model
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
     projects = fields.Many2many('project.project', string="Projects", required=True)

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     #If Sprint is moved to complete, disassociate any child tasks that are not completed.
     @api.onchange('status')
     def onchange_status(self):
         if self.status == 'closed':
            for record in self.project_tasks:
                if record.stage_id.is_closed == False:
                    #record.sprint_id = False
                    record.write({'record.sprint_id': False})
