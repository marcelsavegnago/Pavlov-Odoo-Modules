from odoo import models, fields, api

class BWChangeOwner(models.Model):
    _name = 'bwchange.owner'
    _order = 'owner_sequence'

    #General
    name = fields.Char(string="Owner", required=True)
    owner_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('bwchange.owner') or '/'
        vals['owner_sequence'] = seq
        return super(BWChangeOwner, self).create(vals)
