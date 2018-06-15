from odoo import models, fields

#Main Agreement Records Model
class Agreement(models.Model):
     _name = 'partner_agreement.agreement'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     agreementtemplate = fields.Many2one('partner_agreement.agreement', string="Agreement Template")
     is_template = fields.Boolean(string="Is a Template?")
     version = fields.Integer(string="Version")
     revision = fields.Integer(string="Revision")
     description = fields.Text(string="Description")
     start_date = fields.Date(string="Start Date")
     end_date = fields.Date(string="End Date")

     type = fields.Many2one('partner_agreement.type', string="Agreement Type")
     subtype = fields.Many2one('partner_agreement.subtype', string="Agreement Sub-type")
     status = fields.Many2one('partner_agreement.status', string="Status")
     account_manager = fields.Many2one('res.users', string="Account Manager")
     parent_agreement = fields.Many2one('partner_agreement.agreement', string="Parent Agreement")

     sections = fields.One2many('partner_agreement.section', 'agreement', string="Sections", copy=True)
     clauses = fields.One2many('partner_agreement.clause', 'agreement', string="Clauses", copy=True)
     serviceprofiles = fields.One2many('partner_agreement.serviceprofile', 'agreement', string="Service Profiles", copy=True)
