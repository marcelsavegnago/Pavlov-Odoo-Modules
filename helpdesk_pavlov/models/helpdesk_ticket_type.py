from odoo import models, fields, api

class HelpdeskTicketType(models.Model):

    _inherit = 'helpdesk.ticket.type'

#General
    scope_ids = fields.Many2many('helpdesk.scope', 'scope', string="Scopes", required=False)
