from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ProjectScrumTeam(models.Model):
     _name = 'project.scrum_team'

#General
     name = fields.Char(string="Team Name", required=True)
     user_ids = fields.One2many('res.users', 'user_id', string="Team Members")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]
