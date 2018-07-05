from odoo import models, fields

class EquipmentModel(models.Model):
    _name = 'equipment.model'

    name = fields.Char(string="Title", required=True)
    manufacturer = fields.Many2one('res.partner', string="Manufacturer")
    pec = fields.Char(string="PEC")
    ru_size = fields.Integer(string="RU Size")
    max_shelves = fields.Integer(string="Max Shelves")
    slots = fields.One2many('equipment.slot', 'model', string="Slots")
