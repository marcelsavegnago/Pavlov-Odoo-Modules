from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    milestones = fields.One2many('project.milestone', 'project_id', string="Milestones")
    use_milestones = fields.Boolean(string="Use Milestones")
