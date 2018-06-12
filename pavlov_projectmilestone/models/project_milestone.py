from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ProjectMilestone(models.Model):
     _name = 'pavlov_projectmilestone.milestones'

#General
     name = fields.Char(string="Title", required=True)
     target_date = fields.Date(string="Target Date", required=False)
     actual_date = fields.Date(string="Actual Date", required=False)
     percent_complete = fields.Integer(string="Percent Complete")

     projects = fields.Many2one('project.project', string="Projects")
     project_tasks = fields.One2many('project.task', 'milestone', string="Project Tasks")
