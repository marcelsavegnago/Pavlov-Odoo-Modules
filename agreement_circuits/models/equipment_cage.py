from odoo import models, fields

class EquipmentCage(models.Model):
    _name = 'equipment.cage'

    name = fields.Char(string="Label", required=True)
    site = fields.Many2one('res.partner', string="Site")
    location = fields.Char(string="Location")
    client = fields.Many2one('res.partner', string="Client")
    aka = fields.Char(string="Aka")
    audit_complete = fields.Boolean(string="Audit Complete")
    door_side = fields.Selection([('east', 'East'),('north', 'North'),('south', 'South'),('west', 'West')], string="Door Side")
    width = fields.Char(string="Width")
    depth = fields.Char(string="Depth")
    height = fields.Char(string="Height")
    description = fields.Text(string="Description")
    racks = fields.One2many('equipment.rack', 'cage', string="Cage")
