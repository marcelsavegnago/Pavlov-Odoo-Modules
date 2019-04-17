from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    service_location_unit_id = fields.Many2one('fsm.location',
                                               string="Unit")
    room = fields.Char(string="Room")
    spacer = fields.Char(string=" ", readonly = True)

    @api.onchange('service_location_id')
    def on_change_service_location_id(self):
        if self.service_location_id:
            self.street = self.service_location_id.street
            self.city = self.service_location_id.city
            self.state_id = self.service_location_id.state_id
            self.zip = self.service_location_id.zip
            self.country_id = self.service_location_id.country_id
        else:
            self.street = False
            self.city = False
            self.state_id = False
            self.zip = False
            self.country_id = False

    @api.onchange('service_location_unit_id')
    def on_change_service_location_unit_id(self):
        if self.service_location_unit_id:
            self.street2 = self.service_location_unit_id.name
        else:
            self.street2 = False
