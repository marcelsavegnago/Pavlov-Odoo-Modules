from odoo import models, fields, api

class Agreement(models.Model):

    _inherit = 'partner_agreement.agreement'

    serviceprofiles = fields.One2many('partner_agreement_serviceprofile.serviceprofile', 'name', string="Service Profiles")
