from odoo import models, fields, api

class HelpdeskSeverity(models.Model):
    _name = 'helpdesk.severity'

#General
    name = fields.Char(string="Severity", required=True)
