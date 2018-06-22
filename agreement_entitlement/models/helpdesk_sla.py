from odoo import models, fields, api

class SLA(models.Model):

    _inherit = 'helpdesk.sla'

    entitlements = fields.One2many('agreement_entitlement.entitlement', 'name', string="Entitlements")
