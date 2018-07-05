from odoo import models, fields

class EquipmentSlot(models.Model):
    _name = 'equipment.slot'

    name = fields.Char(string="Label", required=True)
    port_label = fields.Char(string="Port Label (Optional)", required=True)
    slot_type = fields.Many2one('equipment.slottype', string="Slot Type")
    sub_slots = fields.Selection([('no_subslots', 'No Sub-Slots'),('two_subslot', '2 Sub-Slots'),('four_subslot', '4 Sub-Slots'),('six_subslot', '6 Sub-Slots')], string="Circuit Type")
    model = fields.Many2one('equipment.model', string="Model")
