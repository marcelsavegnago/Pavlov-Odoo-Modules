from odoo import models, fields, api

class HelpdeskCloseCode(models.Model):
    _name = 'helpdesk.closecode'

#General
    name = fields.Char(string="Topic", required=True)
    ticket_topic = fields.Many2one('helpdesk.topic', string="Topic", required=True)
    ticket_type_id = fields.Many2one('helpdesk.ticket.type', string="Ticket Type", required=True)
