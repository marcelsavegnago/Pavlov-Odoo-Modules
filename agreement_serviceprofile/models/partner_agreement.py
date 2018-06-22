from odoo import models, fields, api

class Agreement(models.Model):

    _inherit = 'partner_agreement.agreement'

    serviceprofiles = fields.One2many('agreement_serviceprofile.serviceprofile', 'name', string="Service Profiles")
