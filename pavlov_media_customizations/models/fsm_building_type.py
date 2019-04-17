from odoo import models, fields, api

class FSMBuildingType(models.Model):
    _name = 'fsm.building_type'
    _order = 'sequence'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")
