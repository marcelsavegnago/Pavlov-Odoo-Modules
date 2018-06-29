from odoo import models, fields

class EquipmentPhysicalPort(models.Model):
    _name = 'equipment.phyport'

    name = fields.Char(string="Title", required=True)
    equipment = fields.Many2one('maintenance.equipment', string="Equipment")
