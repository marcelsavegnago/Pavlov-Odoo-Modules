from odoo import models, fields

#Main Agreement Section Records Model
class AgreementStatus(models.Model):
     _name = 'partner_agreement.status'

#General
     name = fields.Char(string="Title", required=True)
