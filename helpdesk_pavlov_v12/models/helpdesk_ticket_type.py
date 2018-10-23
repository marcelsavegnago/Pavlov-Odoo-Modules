from odoo import models, fields, api

class HelpdeskTicketType(models.Model):

    _inherit = 'helpdesk.ticket.type'

#General
    scope_ids = fields.Many2many('helpdesk.scope', 'scope', string="Scopes", required=False)
    myproperties_show = fields.Boolean(string="Show in MyProperties", help="If checked, then myproperties will show these tickets.")
    default_priority = fields.Selection([('0','All'),('1','Low priority'),('2','High priority'),('3','Urgent'),], string="Default Priority")
