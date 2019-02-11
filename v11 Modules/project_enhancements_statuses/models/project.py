from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

# GLOBAL ENHANCEMENTS
    project_status = fields.Many2one('project.status',
                                      string="Project Status",
                                      help="Project status options are global status, configured in the Configuration menu.")
