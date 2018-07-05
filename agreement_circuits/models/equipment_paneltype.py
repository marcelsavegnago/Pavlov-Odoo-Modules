from odoo import models, fields

class EquipmentPanelType(models.Model):
    _name = 'equipment.paneltype'

    name = fields.Char(string="Name", required=True)
    cabling = fields.Char(string="Cabling")
