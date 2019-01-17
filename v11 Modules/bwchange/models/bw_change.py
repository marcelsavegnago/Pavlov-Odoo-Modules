from odoo import models, fields, api

class BandwidthChange(models.Model):
     _name = 'bwchange.change'
     _inherit = ['mail.thread']
     _order = 'bwchange_sequence'

     #General
     spacer = fields.Char()
     state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive')],
        related='stage.default_state',
        rack_visibility='always',
        store=True)
     priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')],
        default='low')
     name = fields.Char(string="Title", required=True)
     partner_id = fields.Many2one('res.partner', string="Partner")
     eta = fields.Date(string="ETA", required=False)
     description = fields.Text(string="Description", required=False)
     color = fields.Integer()
     user_id = fields.Many2one('res.users', string="Assigned To")
     eta = fields.Date(string="ETA")

     #Property Circuit Details (Based on Deployment)
     actual_transport = fields.Float(string="Actual Transport (Mbps)")
     circuit_paid_by = fields.Many2one('bwchange.owner', string="Circuit Paid By")
     sold_transport = fields.Float(string="Sold Transport/DIA Down (OffNet Mbps)",)
     dia_upload = fields.Float(string="DIA Up (OffNet Mbps)")
     tesseractive_service = fields.Boolean(string="Tesseractive Service?")
     tesseractiv_speed = fields.Float(string="Tesseractiv Speed (OnNet Mbps) *If Applicable")
     websnap = fields.Boolean(string="Websnap?")
     circuit_landdate = fields.Date(string="Circuit Land Date")
     circuit_id = fields.Char(string="Circuit ID")

     #Current MDF Equipment (Filled out by NOC)
     router = fields.Many2one('bwchange.speed', string="Router")
     mikrotik = fields.Many2one('bwchange.speed', string="MikroTik")
     distro_switch = fields.Many2one('bwchange.speed', string="Distro Switch (Between Buildings)")
     core_switch = fields.Many2one('bwchange.speed', string="Internal Core Switch (Site Backbone)")
     user_switch = fields.Many2one('bwchange.speed', string="Site User Switch Port Speed")
     trunked = fields.Boolean(string="Trunked?")
     qtree_type = fields.Many2one('bwchange.qtreetype', string="Q-Tree Type")
     implementation_notes = fields.Text(string="Implementation Notes")
     implemented_by = fields.Many2one('res.users', string="Implementd By")
     needs_update = fields.Boolean(string="Needs Update?")
     verified_by = fields.Many2one('res.users', string="Verified By")
     verified_date = fields.Date(string ="Verified Date")
     additional_information = fields.Text(string="Additional Information")
     noc_implemenation_date = fields.Date(string="NOC Implemenation Date")

     #User/Unit Experience (Contracted Info)
     websnap_download = fields.Float(string="Websnap Down (Mbps)")
     package_download = fields.Float(string="User/Unit Package Down (Mbps)")
     package_upload = fields.Float(string="User/Unit Package Up (Mbps)")
     unregistered_tesseractiv = fields.Float(string="Unreg Tesserativ (Mbps)")
     unregistered_websnap = fields.Float(string="Unreg WebSnap (Mbps)")
     unregistered_download = fields.Float(string="Unreg Down (Mbps)")
     unregistered_upload = fields.Float(string="Unreg Up (Mbps)")
     reason_for_change = fields.Text(string="Reason for Package Change")

     #Contract Information
     contract_signed_date = fields.Date(string="Contract Signed Date")

     #Finalized Document
     final_document = fields.Binary(string="Final Document")
     filename = fields.Char(string="Filename")

     bwchange_sequence = fields.Integer(string="Sequence")
     #Used for Sequencing
     @api.model
     def create(self, vals):
         seq = self.env['ir.sequence'].next_by_code('bwchange.change') or '/'
         vals['bwchange_sequence'] = seq
         return super(BandwidthChange, self).create(vals)

     #Used for Kanban grouped_by view
     @api.model
     def _read_group_stage_ids(self,stages,domain,order):
         stage_ids = self.env['bwchange.stage'].search([])
         return stage_ids

     stage = fields.Many2one('bwchange.stage',
                             string="Stage",
                             group_expand='_read_group_stage_ids',
                             help="Select the current stage of the Bandwidth Change.")
