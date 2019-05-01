from odoo import models, fields


class FSMLocation(models.Model):
    _inherit = 'fsm.location'

    buildings = fields.Integer(string="Buildings")
    units = fields.Integer(string="Units")
    beds = fields.Integer(string="Beds")
    clubhouse_buildings = fields.Integer(string="Clubhouse Buildings")
    maintenance_buildings = fields.Integer(string="Maintenance Buildings")
    retail_spaces = fields.Integer(string="Retail Spaces")
    construction_type = fields.Many2one('fsm.construction_type',
                                        string="Construction Type")
    building_style = fields.Many2one('fsm.building_style',
                                     string="Building Style")
    resident_type = fields.Many2one('fsm.resident_type',
                                    string="Resident Type")
