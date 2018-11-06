from odoo import models, fields, api

class BandwidthChange(models.Model):
     _name = 'bwchange.change'

     #General
     state = fields.Selection([('new', 'New'),('progress', 'In progress'),('finished', 'Done')],default='new',track_visibility='always')
     priority = fields.Selection([('low', 'Low'),('medium', 'Medium'),('high', 'High'),('urgent', 'Urgent')],default='low')
     name = fields.Char(string="Title", required=True)
     partner_id = fields.Many2one('res.partner', string="Partner")
     eta = fields.Date(string="ETA", required=False)
     description = fields.Text(string="Description", required=False)
     color = fields.Integer()
     #Property Circuit Details (Based on Deployment)
     actual_transport = fields.Float(string="Actual Transport Speed (Mbps)", store=True)
     circuit_paid_by = fields.Many2one ('bwchange.owner',string="Circuit Paid By")
     sold_transport = fields.Float(string="Sold Transport Speed/DIA Download (OffNet Mbps)", store=True)
     dia_upload = fields.Float(string="DIA Upload (OffNet Mbps)", store=True)
     tesseractive_service = fields.Boolean(string="Tesseractive Service?")
     tesseractiv_speed = fields.Float(string="Tesseractiv Speed (OnNet Mbps) *If Applicable", store=True)
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
     verified_by = fields.Many2one('res.users', string="Verified By")
     verified_date = fields.Date(string ="Verified Date")
     #User/Unit Experience (Contracted Info)
     websnap_download = fields.Float(string="Websnap Download Speed (Mbps)", store=True)
     package_download = fields.Float(string="User/Unit Package Download Speed (Mbps)", store=True)
     package_upload = fields.Float(string="User/Unit Package Upload Speed (Mbps)", store=True)
     unregistered_tesseractiv = fields.Float(string="Unregistered Tesserativ (Mbps)", store=True)
     unregistered_websnap = fields.Float(string="Unregistered WebSnap (Mbps)", store=True)
     unregistered_download = fields.Float(string="Unregistered Download (Mbps)", store=True)
     unregistered_upload = fields.Float(string="Unregistered Upload (Mbps)", store=True)
     reason_for_change = fields.Text(string="Reason for Package Change")
     #Contract Information
     contract_signed_date = fields.Date(string="Contract Signed Date")

     #Used for Kanban grouped_by view
     @api.model
     def _read_group_stage_ids(self,stages,domain,order):
         stage_ids = self.env['bwchange.stage'].search([])
         return stage_ids

     stage = fields.Many2one('bwchange.stage', string="Stage", group_expand='_read_group_stage_ids', help="Select the current stage of the agreement.")
