from odoo import models, fields, api

class BWChangeQTreeType(models.Model):
    _name = 'bwchange.qtreetype'
    _order = 'qtreetype_sequence'

    #General
    name = fields.Char(string="Q-Tree Type", required=True)
    qtreetype_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('bwchange.qtreetype') or '/'
        vals['qtreetype_sequence'] = seq
        return super(BWChangeQTreeType, self).create(vals)
