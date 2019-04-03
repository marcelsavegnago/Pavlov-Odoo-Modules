from odoo import models, fields

class Project(models.Model):
    _inherit = 'project.project'

    tag_ids = fields.Many2many('project.tags', string="Tags",)
