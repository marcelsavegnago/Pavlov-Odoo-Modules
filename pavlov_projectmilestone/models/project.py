from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    milestones = fields.Many2many('pavlov_projectmilestone.milestones', string="Milestones")
