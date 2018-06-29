from odoo import models, fields

class EquipmentMediaType(models.Model):
    _name = 'equipment.mediatype'

    name = fields.Char(string="Name", required=True)
