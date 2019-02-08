from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    department_id = fields.Many2one('hr.department',
                                 string="Department",
                                 help="The department that this Project is related to.")
