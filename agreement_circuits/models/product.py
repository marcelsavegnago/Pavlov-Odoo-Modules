from odoo import models, fields

class Product(models.Model):

    _inherit = 'product.template'

    manufacturer = fields.Many2one('res.partner', string="Manufacturer")
    dcim_equipment = fields.Boolean(string="Use in DCIM?", help="Should the product be used in the Maintenance/Equipment App")
    slots = fields.One2many('equipment.slot', 'product', string="Slots")
    port_definitions = fields.One2many('equipment.portdefinition', 'product', string="Port Definitions")
    dcim_product_type = fields.Selection([('wired','Wired Device (Switches, Routers, Etc)'),('wireless','Wireless Device'),('chassis','Chassis'),('rack','Rack'),('shelf','Shelf'),('card','Card'),('pluggable','Pluggable'),('cage','Cage')], string="DCIM Equipment Type")
