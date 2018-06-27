from odoo import models, fields, api

#Main Agreement Records Model
class Agreement(models.Model):
     _name = 'partner_agreement.agreement'

#General
     name = fields.Char(string="Title", required=True)
     is_template = fields.Boolean(string="Is a Template?", default=False, copy=False, help="Make this agreement a template.")
     version = fields.Integer(string="Version", default=1, help="The versions are used to keep track of document history and previous versions can be referenced.", copy=False)
     revision = fields.Integer(string="Revision", default=0, help="The revision will increase with every save event.", copy=False)
     description = fields.Text(string="Description", help="Description of the agreement")
     start_date = fields.Date(string="Start Date", help="When the agreement starts.")
     end_date = fields.Date(string="End Date", help="When the agreement ends.")
     color = fields.Integer()
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")
     company_signed_date = fields.Date(string="Company Signed Date", help="Date the contract was signed by Company.")
     customer_signed_date = fields.Date(string="Customer Signed Date", help="Date the contract was signed by Customer.")
     term = fields.Integer(string="Term (Months)", help="Number of months this agreement/contract is in effect")
     expiration_notice = fields.Integer(string="Exp. Notice (Days)", help="Number of Days before expiration to be notified")
     change_notice = fields.Integer(string="Change Notice (Days)", help="Number of Days to be notified before changes")
     special_terms = fields.Text(string="Special Terms", help="Any terms that you have agreed to and want to track on the agreement/contract")
     contract_value = fields.Integer(string="Contract Value", help="Total value of the contract over ther entire term.")

     account = fields.Many2one('res.partner', string="Account", copy=True, help="Select the customer or vendor account this agreement is related to.")
     type = fields.Many2one('partner_agreement.type', string="Agreement Type", help="Select the type of agreement.")
     subtype = fields.Many2one('partner_agreement.subtype', string="Agreement Sub-type", help="Select the sub-type of this agreement. Sub-Types are related to agreement types.")
     sale_order = fields.Many2one('sale.order', string="Sales Order", help="Select the Sales Order that this agreement is related to.", copy=False)
     payment_term = fields.Many2one('account.payment.term', string="Payment Term", help="Terms of payments.")
     assigned_to = fields.Many2one('res.users', string="Account Manager", help="Select the user who manages this agreement.")
     company_signed_by = fields.Many2one('res.users', string="Signed By", help="The user at our company who authorized/signed the agreement or contract.")
     customer_signed_by = fields.Many2one('res.partner', string="Customer Signed By", help="Contact on the account that signed the agreement/contract.")
     parent_agreement = fields.Many2one('partner_agreement.agreement', string="Parent Agreement", help="Link this agreement to a parent agreement. For example if this agreement is an amendment to another agreement. This list will only show other agreements related to the same account.")

     #order_lines = fields.One2many(related='sale_order.sale_order_line')
     sections = fields.One2many('partner_agreement.section', 'agreement', string="Sections", copy=True)
     clauses = fields.One2many('partner_agreement.clause', 'agreement', string="Clauses", copy=True)
     previous_version_agreements = fields.One2many('partner_agreement.agreement', 'parent_agreement', string="Child Agreements", copy=False, domain=[('active', '=', False)])

     products = fields.Many2many('product.template', string="Products", copy=False)

     state = fields.Selection([('draft', 'Draft'),('progress', 'In progress'),('active', 'Active')], default='draft', track_visibility='always')

     #Used for Kanban grouped_by view
     @api.model
     def _read_group_stage_ids(self,stages,domain,order):
         stage_ids = self.env['partner_agreement.stage'].search([])
         return stage_ids

     stage = fields.Many2one('partner_agreement.stage', string="Stage", group_expand='_read_group_stage_ids', help="Select the current stage of the agreement.")

     #Create New Version Button
     @api.multi
     def create_new_version(self):
         self.write({'state': 'draft'})
         self.copy(default={'name': self.name + ' - OLD VERSION', 'active': False, 'parent_agreement': self.id})
         self.write({'version': self.version + 1})
         self.write({'revision': 0})

     def create_new_agreement(self):
         res = self.copy(default={'name': 'NEW', 'active': True, 'version': 1, 'revision': 0, 'state': 'draft', 'start_date': "", 'end_date':""})
         return {'res_model': 'partner_agreement.agreement', 'type': 'ir.actions.act_window', 'view_mode': 'form', 'view_type': 'form', 'res_id': res.id}

     #Increments the revision on each save action
     def write(self, vals):
         vals['revision'] = self.revision + 1
         return super(Agreement, self).write(vals)
