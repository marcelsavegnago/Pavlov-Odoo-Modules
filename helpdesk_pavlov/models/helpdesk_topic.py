from odoo import models, fields, api

class HelpdeskTopic(models.Model):
    _name = 'helpdesk.topic'

#General
    name = fields.Char(string="Topic", required=True)
    ticket_type_id = fields.Many2one('helpdesk.ticket.type', string="Ticket Type", required=True)
