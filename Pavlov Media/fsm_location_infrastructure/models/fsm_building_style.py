from odoo import models, fields, api


class FSMBuildingStyle(models.Model):
    _name = 'fsm.building_style'
    _order = 'sequence'
    _description = 'Building Style'

    name = fields.Char(string="Style", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('fsm.building_style') or 0
        vals['sequence'] = seq
        return super(FSMBuildingStyle, self).create(vals)
