from odoo import models, fields, api

class Helpdesk(models.Model):

    _inherit = 'helpdesk.ticket'

#General
    spacer = fields.Char(string=" ")
    sitecode = fields.Char(string="Site Code")
    location_onsite = fields.Char(string="Location On-Site")
    linked_nodes = fields.Text(string="Linked Nodes")

    topic = fields.Many2one('helpdesk.topic', string="Topic", required=True)
    parent_ticket = fields.Many2one('helpdesk.ticket', string="Parent Ticket")
    parent_location = fields.Many2one(related='partner_id.parent_id', string="Parent Location")
    customer_type = fields.Selection(related='partner_id.company_type', string="Customer Type")

    maintenance_start = fields.Date(string="Maint. Start", required=False)
    maintenance_end = fields.Date(string="Maint. End", required=False)
    maintenance_outage_duration = fields.Integer(string="Outage Duration")
    maintenance_impact = fields.Selection([('low', 'Low - Little to No Risk'),('medium', 'Medium - Moderate Risk'),('high', 'High - Certain Risk')], default='low')

    customer_street = fields.Char(related='partner_id.street', string="Street")
    customer_street2 = fields.Char(related='partner_id.street2', string="Street 2")
    customer_city = fields.Char(related='partner_id.city', string="City")
    customer_state = fields.Many2one(related='partner_id.state_id', string="State")
    customer_zip = fields.Char(related='partner_id.zip', string="Zip")
    customer_phone = fields.Char(related='partner_id.phone', string="Phone")
    customer_mobile = fields.Char(related='partner_id.mobile', string="Mobile")
    customer_email = fields.Char(related='partner_id.email', string="Email")
    customer_website = fields.Char(related='partner_id.website', string="Website")

    parent_location_street = fields.Char(related='parent_location.street', string="Street")
    parent_location_street2 = fields.Char(related='parent_location.street2', string="Street 2")
    parent_location_city = fields.Char(related='parent_location.city', string="City")
    parent_location_state = fields.Many2one(related='parent_location.state_id', string="State")
    parent_location_zip = fields.Char(related='parent_location.zip', string="Zip")
    parent_location_phone = fields.Char(related='parent_location.phone', string="Phone")
    parent_location_mobile = fields.Char(related='parent_location.mobile', string="Mobile")
    parent_location_email = fields.Char(related='parent_location.email', string="Email")
    parent_location_website = fields.Char(related='parent_location.website', string="Website")

    resolution = fields.Text(string="Resolution")
    review_reason = fields.Char(string="Ticket Review Reason")
