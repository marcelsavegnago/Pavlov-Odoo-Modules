from odoo import models, fields

#Main Agreement clause Records Model
class AgreementClause(models.Model):
     _name = 'partner_agreement.clause'
     _order = 'sequence'

#General
     name = fields.Char(string="Title", required=True)
     sequence = fields.Integer(string="Sequence")
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement")
     section = fields.Many2one('partner_agreement.section', string="Section")
     content = fields.Html(string="Clause Content")
     parent_id = fields.Many2one('partner_agreement.clause', string="Parent Clause")

#Used for the dynamic placeholder generator
     model_id = fields.Many2one('ir.model', string="Applies to")
     model_object_field = fields.Many2one('ir.model.fields')
     sub_object = fields.Many2one('ir.model', string="Sub-model")
     sub_model_object_field = fields.Many2one('ir.model.fields')
     null_value = fields.Char(string="Default Value")
     copyvalue = fields.Char(string="Placeholder Expression")
