from odoo import models, fields

class EquipmentPortDefinition(models.Model):
    _name = 'equipment.portdefinition'

    name = fields.Char(string="Title", required=True)
    port_count = fields.Integer(string="Port Count")
    nomenclature = fields.Selection([('sequential', 'Sequential'),('custom', 'Custom')], string="Nomenclature")
    first_port_num = fields.Integer(string="1st Port Number")
    numbering = fields.Selection([('serial', 'Serial'),('slot_daughter_port_sequential', 'Slot / Daughter / Port Seqential')], string="Numbering")
    default_protocol = fields.Many2one('equipment.portprotocol', string="Default Protocol")
    default_media = fields.Many2one('equipment.mediatype', string="Default Media")
    media_types = fields.Many2many('equipment.mediatype', string="Media Types")
    protocols = fields.Many2many('equipment.portprotocol', string="Protocols")
    card = fields.Many2one('equipment.portdefinition', string="Card")
    sequence = fields.Integer(string="Sequence")
    product = fields.Many2one('product.template', string="Product")
