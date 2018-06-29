from odoo import models, fields

class EquipmentSlotType(models.Model):
    _name = 'equipment.slottype'

    name = fields.Char(string="Title", required=True)
    allow_connections = fields.Boolean(string="Allow Connections")
