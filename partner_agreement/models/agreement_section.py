from odoo import models, fields

#Main Agreement Section Records Model
class AgreementSection(models.Model):
     _name = 'partner_agreement.section'
     _order = 'sequence'

#General
     name = fields.Char(string="Title", required=True)
     sequence = fields.Integer(string="Sequence")
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement")
     clauses = fields.One2many('partner_agreement.clause', 'section', string="Clauses")
     content = fields.Html(string="Section Content")
     parent_id = fields.Many2one('partner_agreement.section', string="Parent Section")
