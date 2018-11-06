from odoo import models, fields, api, tools, _

class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'

#General
    spacer = fields.Char(string=" ")
    sitecode = fields.Char(string="Site Code")
    location_onsite = fields.Char(string="Location On-Site")
    linked_nodes = fields.Text(string="Linked Nodes")
    source = fields.Many2one('helpdesk.source', string="Source", required=True)
    service_location_tickets = fields.Integer('Location Tickets', compute='_compute_service_location_tickets')

    scope = fields.Many2one('helpdesk.scope', string="Scope", required=True)
    parent_ticket = fields.Many2one('helpdesk.ticket', string="Parent Ticket")
    service_location = fields.Many2one(related='partner_id.parent_id', string="Service Location")
    partner_type = fields.Selection(related='partner_id.company_type', string="Partner Type")

    maintenance_start = fields.Date(string="Maint. Start", required=False)
    maintenance_end = fields.Date(string="Maint. End", required=False)
    maintenance_outage_duration = fields.Integer(string="Outage Duration")
    maintenance_impact = fields.Selection([('low', 'Low - Little to No Risk'),('medium', 'Medium - Moderate Risk'),('high', 'High - Certain Risk')], default='low')

    partner_street = fields.Char(related='partner_id.street', string="Street")
    partner_street2 = fields.Char(related='partner_id.street2', string="Street 2")
    partner_city = fields.Char(related='partner_id.city', string="City")
    partner_state = fields.Many2one(related='partner_id.state_id', string="State")
    partner_zip = fields.Char(related='partner_id.zip', string="Zip")
    partner_phone = fields.Char(related='partner_id.phone', string="Phone")
    partner_mobile = fields.Char(related='partner_id.mobile', string="Mobile")
    partner_website = fields.Char(related='partner_id.website', string="Website")

    resolution = fields.Text(string="Resolution")
    close_code = fields.Many2one('helpdesk.closecode', string="Close Code")
    review_reason = fields.Char(string="Ticket Review Reason")

    track_created_email = fields.Boolean(string="Ticket Created Email")
    track_monitoring_email = fields.Boolean(string="Ticket Monitoring Email")
    track_outagereleated_email = fields.Boolean(string="Ticket Related to Outage Email")
    track_closed_email = fields.Boolean(string="Ticket Closed Email")

    @api.onchange('ticket_type_id')
    def _onchange_priority(self):
            self.priority = self.ticket_type_id.default_priority

    @api.depends('service_location')
    def _compute_service_location_tickets(self):
        for ticket in self:
            ticket_data = self.env['helpdesk.ticket'].read_group([
                ('partner_id', '=', ticket.service_location.id),
                ('stage_id.is_close', '=', False)
            ], ['partner_id'], ['partner_id'])
            if ticket_data:
                ticket.service_location_tickets = ticket_data[0]['partner_id_count']

    @api.multi
    def open_service_location_tickets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Location Tickets'),
            'res_model': 'helpdesk.ticket',
            'view_mode': 'kanban,tree,form,pivot,graph',
            'context': {'search_default_is_open': True, 'search_default_partner_id': self.service_location.id}
        }
