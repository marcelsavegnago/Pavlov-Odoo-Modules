from odoo import models, fields, api

class Partner(models.Model):

    _inherit = 'res.partner'

    entitlements = fields.One2many('agreement_entitlement.entitlement', 'name', string="Entitlements")
    equipments = fields.One2many('maintenance.equipment', 'customer', string="Equipment")
