from odoo import models, fields, api

class ProjectForecast(models.Model):
    _inherit = 'project.forecast'

    sprint_id = fields.Many2one(related='task_id.sprint_id',
                                string="Sprint",
                                store=True,
                                readonly=False)
