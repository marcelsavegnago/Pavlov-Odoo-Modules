from odoo import models, fields, api

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

#Placeholder fields
     model_id = fields.Many2one('ir.model', string="Applies to", help="The type of document this template can be used with.")
     model_object_field = fields.Many2one('ir.model.fields', string="Field", help="Select target field from the related document model. If it is a relationship field you will be able to select a target field at the destination of the relationship.")
     sub_object = fields.Many2one('ir.model', string="Sub-model", help="When a relationship field is selected as first field, this field shows the document model the relationship goes to.")
     sub_model_object_field = fields.Many2one('ir.model.fields', string="Sub-field", help="When a relationship field is selected as first field, this field lets you select the target field within the destination document model (sub-model).")
     null_value = fields.Char(string="Default Value", help="Optional value to use if the target field is empty.")
     copyvalue = fields.Char(string="Placeholder Expression", help="Final placeholder expression, to be copy-pasted in the desired template field.")
#compute="_comp_copyvalue"
#Compute fields
#    @api.one
#    @api.onchange('model_object_field','null_value')
#    def _comp_copyvalue(self):
#        self.copyvalue = '${object.' + str(self.model_object_field.name) + '}'

#    @api.depends('model_object_field', 'null_value')
#    def _comp_copyvalue(self):
#        if self.model_object_field.name == True and self.null_value == False:
#            self.copyvalue = '${object.' + self.model_object_field.name + '}'
#        else self.model_object_field.name == True and self.null_value == True:
#            self.copyvalue = '${object.' + self.model_object_field.name + ' or ' + self.null_value + '}'
#        else:
#            self.copyvalue = ''
