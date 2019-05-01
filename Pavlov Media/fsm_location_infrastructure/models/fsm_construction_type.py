from odoo import models, fields, api


class FSMConstructionType(models.Model):
    _name = 'fsm.construction_type'
    _order = 'sequence'
    _description = 'Building Type'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code(
            'fsm.construction_type') or 0
        vals['sequence'] = seq
        return super(FSMConstructionType, self).create(vals)
