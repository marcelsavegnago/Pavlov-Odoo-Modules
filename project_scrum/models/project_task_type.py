from odoo import models, fields, api

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    is_closed = fields.Boolean(string="Is Closing Stage")
