from odoo import models, fields

class EquipmentPhysicalPort(models.Model):
    _name = 'equipment.phyport'

    name = fields.Char(string="Number", required=True, help="The Number of the port.")
    description = fields.Char(string="Description",help="The name of the port (if applicable).")
    equipment = fields.Many2one('maintenance.equipment', string="Equipment", help="The equipment this port is on.")
    connected_to_equipment = fields.One2many('maintenance.equipment', 'port_connected_to', string="Equipment Connected To", help="If port is connected to another equipment.")
    
