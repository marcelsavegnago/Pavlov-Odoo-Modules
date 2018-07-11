from odoo import models, fields

class Partner(models.Model):

    _inherit = 'res.partner'

    circuit_segments = fields.One2many('agreement_circuits.segment', 'name', string="Circuit Segments")
    equipments = fields.One2many('maintenance.equipment', 'customer', string="Equipment")
