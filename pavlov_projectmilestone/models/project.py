from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    milestones = fields.One2many('pavlov_projectmilestone.milestones', 'projects', string="Milestones")
