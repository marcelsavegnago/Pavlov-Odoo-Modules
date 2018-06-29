from odoo import models, fields

class EquipmentCard(models.Model):
    _name = 'equipment.card'

    name = fields.Char(string="Name", required=True)
    aka = fields.Char(string="AKA", required=True)
    pec = fields.Char(string="PEC", help="Product Equipment Code")
    default_port_status = fields.Selection([('faulty', 'Faulty'),('in_service', 'In Service'),('out_of_service', 'Out of Service'),('un_equipped', 'Un-Equipped')], string="Default Port Status")
    type = fields.Selection([('normal', 'Normal'),('daughter_card', 'Daughter Card'),('mother_card', 'Mother Card')], string="Type")
    num_daughter_cards = fields.Integer(string="# of Daughter Cards") #will want invisible if type != mothercard
    daughter_card_label_start = fields.Char(string="Label Start", help="Daughter Slot Label")
    size = fields.Selection([('one', '1 Slot'),('half', '1/2 Slot'),('fourth', '1/4 Slot'),('sixth', '1/6 Slot'),('two', '2 Slot'),('three', '3 Slot'),('four', '4 Slot')], string="Default Port Status")
