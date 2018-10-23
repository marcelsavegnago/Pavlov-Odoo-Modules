from odoo import models, fields, api

class HelpdeskCloseCode(models.Model):
    _name = 'helpdesk.closecode'

#General
    name = fields.Char(string="Close Code", required=True)
    ticket_scope = fields.Many2one('helpdesk.scope', string="Scope", required=True)
    ticket_type_id = fields.Many2one('helpdesk.ticket.type', string="Ticket Type", required=True)
