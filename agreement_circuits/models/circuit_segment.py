from odoo import models, fields

class CircuitSegment(models.Model):
    _name = 'agreement_circuits.segment'

    name = fields.Char(string="Title", required=True)
    internal_circuit_id = fields.Char(string="Internal Circuit ID")
    circuit_type = fields.Selection([('ethernet', 'Ethernet'),('dark_fiber', 'Dark Fiber')], string="Circuit Type")
    pricing_type = fields.Selection([('burstable', 'Burstable'),('fixed_rate', 'Fixed Rate')], string="Pricing Type")
    min_mrc = fields.Integer(string="Minimum MRC")
    price_per_mb = fields.Integer(string="Price / Mb")
    nrc = fields.Integer(string="NRC")
    comments = fields.Text(string="Comments")
    spacer = fields.Char(string="Spacer")

    parent = fields.Many2one('partner_agreement.agreement', string="Parent")

    a_carrier = fields.Many2one('res.partner', string="A Carrier")
    a_endpoint = fields.Many2one('res.partner', string="Name")
    a_endpoint_address = fields.Char(related='a_endpoint.contact_address', string="Address")
    a_endpoint_handoff = fields.Text(string="Handoff")
    a_endpoint_demarc = fields.Text(string="Demarc")
    a_endpoint_extended_demarc = fields.Text(string="Extended Demarc")
    a_facility = fields.Many2one('maintenance.equipment', string="Facility A")

    z_carrier = fields.Many2one('res.partner', string="Z Carrier")
    z_endpoint = fields.Many2one('res.partner', string="Name")
    z_endpoint_address = fields.Char(related='z_endpoint.contact_address', string="Address")
    z_endpoint_handoff = fields.Text(string="Handoff")
    z_endpoint_demarc = fields.Text(string="Demarc")
    z_endpoint_extended_demarc = fields.Text(string="Extended Demarc")
    z_facility = fields.Many2one('maintenance.equipment', string="Facility Z")
