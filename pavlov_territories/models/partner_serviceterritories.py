from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    milestone = fields.Many2one('pavlov_projectmilestone.milestones', string="Milestones")
