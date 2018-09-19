from odoo import models, fields, api

class Helpdesk(models.Model):

    _inherit = 'helpdesk.ticket'

#General
    spacer = fields.Char(string=" ")
    sitecode = fields.Char(string="Site Code")
    location_onsite = fields.Char(string="Location On-Site")
    linked_nodes = fields.Text(string="Linked Nodes")

    origin = fields.Many2one('helpdesk.origin', string="Origin", required=True)
    severity = fields.Many2one('helpdesk.severity', string="Severity", required=True)
    service_location = fields.Many2one('res.partner', string="Service Location", required=True)
    contact = fields.Many2one('res.partner', string="Contact")

    maintenance_start = fields.Date(string="Maint. Start", required=False)
    maintenance_end = fields.Date(string="Maint. End", required=False)
    maintenance_outage_duration = fields.Integer(string="Outage Duration")
    maintenance_impact = fields.Selection([('low', 'Low - Little to No Risk'),('medium', 'Medium - Moderate Risk'),('high', 'High - Certain Risk')], default='draft')

    contact_address = fields.Char(related='contact.contact_address', string="Address")
    contact_street = fields.Char(related='contact.street', string="Street")
    contact_street2 = fields.Char(related='contact.street2', string="Street 2")
    contact_city = fields.Char(related='contact.city', string="City")
    contact_state = fields.Many2one(related='contact.state_id', string="State")
    contact_zip = fields.Char(related='contact.zip', string="Zip")
    contact_phone = fields.Char(related='contact.phone', string="Phone")
    contact_mobile = fields.Char(related='contact.mobile', string="Mobile")
    contact_email = fields.Char(related='contact.email', string="Email")

    service_location_address = fields.Char(related='service_location.contact_address', string="Address")
    service_location_street = fields.Char(related='service_location.street', string="Street")
    service_location_street2 = fields.Char(related='service_location.street2', string="Street 2")
    service_location_city = fields.Char(related='service_location.city', string="City")
    service_location_state = fields.Many2one(related='service_location.state_id', string="State")
    service_location_zip = fields.Char(related='service_location.zip', string="Zip")
    service_location_phone = fields.Char(related='service_location.phone', string="Phone")
    service_location_mobile = fields.Char(related='service_location.mobile', string="Mobile")
    service_location_email = fields.Char(related='service_location.email', string="Email")
    service_location_website = fields.Char(related='service_location.website', string="Website")
