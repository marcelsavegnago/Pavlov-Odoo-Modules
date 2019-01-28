from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# GLOBAL ENHANCEMENTS
    project_status = fields.Many2one('project.status',
                                      string="Status",
                                      help="Project status options are global status, configured in the Configuration menu.")
