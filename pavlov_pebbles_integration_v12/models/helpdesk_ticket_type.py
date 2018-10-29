from odoo import models, fields, api

class HelpdeskTicketType(models.Model):

    _inherit = 'helpdesk.ticket.type'

#General
    myproperties_show = fields.Boolean(string="Show in MyProperties", help="If checked, then myproperties will show these tickets.")
