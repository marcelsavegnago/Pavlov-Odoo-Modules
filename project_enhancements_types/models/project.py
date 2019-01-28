from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# GLOBAL ENHANCEMENTS
    project_type = fields.Many2one('project.type',
                                   string="Project Type",
                                   help="The type of Project",
                                   required=True)
