from odoo import models, fields

class EquipmentPluggableType(models.Model):
    _name = 'equipment.pluggabletype'

    name = fields.Char(string="Name", required=True)
