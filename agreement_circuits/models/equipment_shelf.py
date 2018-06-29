from odoo import models, fields

class EquipmentShelf(models.Model):
    _name = 'equipment.shelf'

    name = fields.Char(string="Name", required=True)
    manufacturer = fields.Char(string="Manufacturer")
    pec = fields.Char(string="PEC")
    ru_size = fields.Char(string="RU Size")
