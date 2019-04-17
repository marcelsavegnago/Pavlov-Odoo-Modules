from odoo import models, fields, api

class FSMResidentType(models.Model):
    _name = 'fsm.resident_type'
    _order = 'sequence'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")
