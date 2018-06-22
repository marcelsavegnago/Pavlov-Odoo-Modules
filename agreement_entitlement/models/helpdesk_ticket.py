from odoo import models, fields, api

class Ticket(models.Model):

    _inherit = 'helpdesk.ticket'

    entitlement = fields.Many2one('agreement_entitlement.entitlement', string="Entitlement")
    equipments = fields.Many2many('maintenance.equipment', string="Equipment")
