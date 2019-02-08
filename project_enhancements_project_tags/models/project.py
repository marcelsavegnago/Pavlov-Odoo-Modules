from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    tag_ids = fields.Many2many('project.tags',
                                 string="Tags",
                                 help="The Tags that this Project is related to.")
