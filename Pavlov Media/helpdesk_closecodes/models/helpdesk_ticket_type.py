from odoo import models, fields


class HelpdeskTicketType(models.Model):
    _inherit = 'helpdesk.ticket.type'

    enable_closecode = fields.Boolean(string="Enable Close Codes",
                                      help="Enable to require cause and \
                                      action taken fields on the ticket when \
                                      this ticket type is selected.")
