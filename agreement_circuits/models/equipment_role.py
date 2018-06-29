from odoo import models, fields

class EquipmentRole(models.Model):
    _name = 'equipment.role'

    name = fields.Char(string="Title", required=True)
