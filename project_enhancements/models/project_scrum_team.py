from odoo import models, fields, api

class ProjectScrumTeam(models.Model):
     _name = 'project.scrum_team'

#General
     name = fields.Char(string="Team Name", required=True)
     user_ids = fields.One2many('res.users', 'user_id', string="Team Members", help="List all users that are part of the scrum team.")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]
