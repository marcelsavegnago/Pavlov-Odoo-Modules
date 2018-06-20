from odoo import models, fields, api

#Main Agreement Section Records Model
class AgreementSection(models.Model):
     _name = 'partner_agreement.section'
     _order = 'section_sequence'

#General
     name = fields.Char(string="Title", required=True)
     section_sequence = fields.Integer(string="Sequence", default=1)
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement", ondelete="cascade")
     clauses = fields.One2many('partner_agreement.clause', 'section', string="Clauses")
     content = fields.Html(string="Section Content")
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")
