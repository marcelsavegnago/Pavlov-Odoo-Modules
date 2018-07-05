from odoo import models, fields

class EquipmentRack(models.Model):
    _name = 'equipment.rack'

    name = fields.Char(string="Title", required=True)
    manufacturer = fields.Many2one('res.partner', string="Manufacturer")
    style = fields.Selection([('two_post_open_frame', '2 Post Open Frame'),('four_post_open_frame', '4 Post Open Frame'),('enclosed', 'Enclosed')], string="Style")
    status = fields.Many2one('equipment.status', string="Status")
    color = fields.Selection([('aqua', 'Aqua'),('black', 'Black'),('blue', 'Blue')], string="Color")
    lockable = fields.Boolean(string="Lockable")
    stackable = fields.Boolean(string="Stackable")
    rear_mount = fields.Boolean(string="Rear Mount?")
    mounting_position = fields.Selection([('floor', 'Floor'),('wall', 'Wall')], string="Mounting Position")
    rack_units = fields.Integer(string="Rack Units")
    width = fields.Char(string="Width")
    depth = fields.Char(string="Depth")
    height = fields.Char(string="Height")
    equipment_width = fields.Char(string="Equipment Width")
    description = fields.Text(string="Description")
    cage = fields.Many2one('equipment.cage', string="Cage")
