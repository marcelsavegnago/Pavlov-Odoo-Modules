from odoo import models, fields

class EquipmentStatus(models.Model):
    _name = 'equipment.status'

    name = fields.Char(string="Name", required=True)
    id = fields.Integer(string="ID")
