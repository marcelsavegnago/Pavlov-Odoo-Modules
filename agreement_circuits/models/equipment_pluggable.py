from odoo import models, fields

class EquipmentPluggable(models.Model):
    _name = 'equipment.pluggable'

    name = fields.Char(string="Name", required=True)
    pec = fields.Float(string="PEC")
    manufacturer = fields.Char(string="Manufacturer")
    sts_time_slot = fields.Integer(string="STS-1 Time Slots")
    type = fields.Many2one('equipment.pluggabletype', string="Type")
