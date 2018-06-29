from odoo import models, fields, api

class Agreement(models.Model):

    _inherit = 'partner_agreement.agreement'

    primary_circuit = fields.Many2one('partner_agreement.agreement', string="Primary Circuit")
    backup_circuit = fields.Many2one('partner_agreement.agreement', string="Backup Circuit")

    tsp_code = fields.Char(string="TSP Code")
    linking_tag = fields.Char(string="Linking Tag")
    alternate_id = fields.Char(string="Alternate ID")
    fiber_count = fields.Integer(string="Fiber Count")
    infrastructure = fields.Boolean(string="Infrastructure")
    channelized = fields.Boolean(string="Channelized")
    protection = fields.Selection([('protected', 'Protected'),('unprotected', 'Unprotected')],string="Protection")
    fiber_type = fields.Selection([('multi_mode', 'Multi-Mode'),('single_mode', 'Single-Mode')], string="Fiber Type")
    port_speed = fields.Integer(string="Port Speed")
    burst_speed = fields.Integer(string="Burst Speed")
    speed_cir = fields.Integer(string="Speed/CIR")
    ninetyfive_usage = fields.Integer(string="95th % Usage")
    ip_address = fields.Text(string="IP Address")
    interface = fields.Char(string="Interface")
    as_number = fields.Char(string="AS Number")
    vlan = fields.Char(string="VLAN")
    spacer = fields.Char(string="Spacer")
