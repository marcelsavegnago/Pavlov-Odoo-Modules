from odoo import models, fields

class EquipmentVirtualPort(models.Model):
    _name = 'equipment.vport'

    name = fields.Char(string="Title", required=True)
    equipment = fields.Many2one('maintenance.equipment', string="Equipment")
