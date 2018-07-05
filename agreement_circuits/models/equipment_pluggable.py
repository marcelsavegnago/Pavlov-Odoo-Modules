from odoo import models, fields

class EquipmentPluggable(models.Model):
    _name = 'equipment.pluggable'

    name = fields.Char(string="Name", required=True)
    pec = fields.Char(string="PEC")
    manufacturer = fields.Many2one('res.partner', string="Manufacturer")
    type = fields.Many2one('equipment.pluggabletype', string="Type")
    applicable_cards = fields.Many2many('equipment.card', string="Applicable Cards")
