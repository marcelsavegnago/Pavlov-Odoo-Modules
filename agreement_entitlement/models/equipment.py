from odoo import models, fields

class Equipment(models.Model):

    _inherit = 'maintenance.equipment'

    entitlement = fields.Many2many('agreement_entitlement.entitlement', string="Entitlement")
    product = fields.Many2one('product.template', string="Product")
    customer = fields.Many2one('res.partner', string="Customer")

    tickets = fields.Many2many('helpdesk.ticket', string="Tickets")
