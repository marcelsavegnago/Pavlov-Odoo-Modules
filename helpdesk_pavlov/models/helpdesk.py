from odoo import models, fields, api

class Helpdesk(models.Model):

    _inherit = 'helpdesk.ticket'

#General
    origin = fields.Many2one('helpdesk.origin', string="Origin", required=True)
    severity = fields.Many2one('helpdesk.severity', string="Severity", required=True)

    #maintenance_start = fields.Date(string="Maint. Start", required=False)
    #maintenance_end = fields.Date(string="Maint. End", required=False)
