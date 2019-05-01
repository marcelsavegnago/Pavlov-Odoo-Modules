from odoo import models, fields, api


class FSMResidentType(models.Model):
    _name = 'fsm.resident_type'
    _order = 'sequence'
    _description = 'Resident Type'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('fsm.resident_type') or 0
        vals['sequence'] = seq
        return super(FSMResidentType, self).create(vals)
