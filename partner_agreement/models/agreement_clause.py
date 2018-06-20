from odoo import models, fields

#Main Agreement clause Records Model
class AgreementClause(models.Model):
     _name = 'partner_agreement.clause'
     _order = 'clause_sequence'

#General
     name = fields.Char(string="Title", required=True)
     clause_sequence = fields.Integer(string="Sequence")
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement", ondelete="cascade")
     section = fields.Many2one('partner_agreement.section', string="Section", ondelete="cascade")
     content = fields.Html(string="Clause Content")
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")

#Used for the dynamic placeholder generator
     model_id = fields.Many2one('ir.model', string="Applies to")
     model_object_field = fields.Many2one('ir.model.fields')
     sub_object = fields.Many2one('ir.model', string="Sub-model")
     sub_model_object_field = fields.Many2one('ir.model.fields')
     null_value = fields.Char(string="Default Value")
     copyvalue = fields.Char(string="Placeholder Expression")
