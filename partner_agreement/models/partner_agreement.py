from odoo import models, fields, api

#Main Agreement Records Model
class Agreement(models.Model):
     _name = 'partner_agreement.agreement'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account", copy=True, help="Select the customer or vendor account this agreement is related to.")
     is_template = fields.Boolean(string="Is a Template?", default=False, copy=False, help="Make this agreement a template.")
     version = fields.Integer(string="Version", default=1, help="The versions are used to keep track of document history and previous versions can be referenced.", copy=False)
     revision = fields.Integer(string="Revision", default=0, help="The revision will increase with every save event.", copy=False)
     description = fields.Text(string="Description", help="Description of the agreement")
     start_date = fields.Date(string="Start Date", help="When the agreement starts.")
     end_date = fields.Date(string="End Date", help="When the agreement ends.")
     color = fields.Integer()
     active = fields.Boolean(string="Active", default=True, help="If unchecked, it will allow you to hide the agreement without removing it.")

     type = fields.Many2one('partner_agreement.type', string="Agreement Type", help="Select the type of agreement.")
     subtype = fields.Many2one('partner_agreement.subtype', string="Agreement Sub-type", help="Select the sub-type of this agreement. Sub-Types are related to agreement types.")

     account_manager = fields.Many2one('res.users', string="Account Manager", help="Select the user who manages this agreement.")
     parent_agreement = fields.Many2one('partner_agreement.agreement', string="Parent Agreement", help="Link this agreement to a parent agreement. For example if this agreement is an amendment to another agreement. This list will only show other agreements related to the same account.")

     sections = fields.One2many('partner_agreement.section', 'agreement', string="Sections", copy=True)
     clauses = fields.One2many('partner_agreement.clause', 'agreement', string="Clauses", copy=True)
     serviceprofiles = fields.One2many('partner_agreement.serviceprofile', 'agreement', string="Service Profiles", copy=True)
     previous_version_agreements = fields.One2many('partner_agreement.agreement', 'parent_agreement', string="Child Agreements", copy=False, domain=[('active', '=', False)])

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
