# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import api, fields, models


class BWChangeOwner(models.Model):
    _name = 'bwchange.owner'
    _order = 'owner_sequence'

    # General
    name = fields.Char(string="Owner", required=True)
    owner_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('bwchange.owner') or '1000'
        vals['owner_sequence'] = seq
        return super(BWChangeOwner, self).create(vals)
