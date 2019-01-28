from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

    department = fields.Many2one('hr.department',
                                 string="Department",
                                 help="The department that this Project is related to.")
