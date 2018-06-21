from odoo import models, fields

#Main Agreement Service Profile Records Model
class AgreementServiceProfile(models.Model):
     _name = 'partner_agreement_serviceprofile.serviceprofile'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement", ondelete="cascade")
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")
