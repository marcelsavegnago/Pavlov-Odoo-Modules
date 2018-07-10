from odoo import models, fields

class EquipmentCircuitType(models.Model):
    _name = 'equipment.circuittype'

    name = fields.Char(string="Name", required=True)
