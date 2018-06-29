from odoo import models, fields

class EquipmentPortProtocol(models.Model):
    _name = 'equipment.portprotocol'

    name = fields.Char(string="Name", required=True)
    mbps = fields.Float(string="Mbps")
    sts_time_slots = fields.Integer(string="STS-1 Time Slots")
