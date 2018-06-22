from odoo import models, fields, api

class Agreement(models.Model):

    _inherit = 'partner_agreement.agreement'

    entitlements = fields.One2many('agreement_entitlement.entitlement', 'name', string="Entitlements")
