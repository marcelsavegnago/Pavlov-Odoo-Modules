from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ProjectMilestone(models.Model):
     _name = 'pavlov_projectmilestone.milestones'

#General
     name = fields.Char(string="Title", required=True)
     start_date = fields.Date(string="Start Date", required=True)
     end_date = fields.Date(string="End Date", required=True)
     percent_complete = fields.Integer(string="Percent Complete")

     projects = fields.Many2many('project.project', 'milestones', string="Projects")
     project_tasks = fields.One2many('project.task', 'milestone', string="Project Tasks")
