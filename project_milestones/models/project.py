from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    milestones = fields.One2many('project_milestones.milestones', 'projects', string="Milestones")
