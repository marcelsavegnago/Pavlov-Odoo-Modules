from odoo import models, fields

#Main Agreement Service Profile Records Model
class AgreementEntitlement(models.Model):
     _name = 'agreement_entitlement.entitlement'

#General
     name = fields.Char(string="Title", required=True)
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")

     account = fields.Many2one('res.partner', string="Account")
     agreement = fields.Many2one('partner_agreement.agreement', string="Agreement", ondelete="cascade")
     helpdesk_sla = fields.Many2one('helpdesk.sla', string="SLA")

     equipments = fields.Many2many('maintenance.equipment', string="Equipments")
