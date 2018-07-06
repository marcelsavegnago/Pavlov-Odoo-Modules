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
    a_image = fields.Binary(related='a_facility.image')
    a_site_contact = fields.Many2one('res.partner', string="Site POC")
    a_phone = fields.Char(related='a_site_contact.phone', string="Phone")
    a_cell = fields.Char(related='a_site_contact.mobile', string="Cell")
    a_fax = fields.Char(string="Fax")
    a_email = fields.Char(related='a_site_contact.email', string="E-mail")
    a_secondary_contact = fields.Many2one('res.partner', string="Secondary POC")
    a_secondary_phone = fields.Char(related='a_secondary_contact.phone', string="Secondary Phone")
    a_loa_cfa = fields.Text(string="LOA/CFA", help="Letter of Authority/Customer Facility Assignment")

    z_carrier = fields.Many2one('res.partner', string="Z Carrier")
    z_endpoint = fields.Many2one('res.partner', string="Name")
    z_endpoint_address = fields.Char(related='z_endpoint.contact_address', string="Address")
    z_endpoint_handoff = fields.Text(string="Handoff")
    z_endpoint_demarc = fields.Text(string="Demarc")
    z_endpoint_extended_demarc = fields.Text(string="Extended Demarc")
    z_facility = fields.Many2one('maintenance.equipment', string="Facility Z")
    z_image = fields.Binary(related='z_facility.image')
    z_site_contact = fields.Many2one('res.partner', string="Site POC")
    z_phone = fields.Char(related='z_site_contact.phone', string="Phone")
    z_cell = fields.Char(related='z_site_contact.mobile', string="Cell")
    z_fax = fields.Char(string="Fax")
    z_email = fields.Char(related='z_site_contact.email', string="E-mail")
    z_secondary_contact = fields.Many2one('res.partner', string="Secondary POC")
    z_secondary_phone = fields.Char(related='z_secondary_contact.phone', string="Secondary Phone")
    z_loa_cfa = fields.Text(string="LOA/CFA", help="Letter of Authority/Customer Facility Assignment")
