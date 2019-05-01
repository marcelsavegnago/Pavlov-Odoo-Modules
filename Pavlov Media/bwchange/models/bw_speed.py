# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import api, fields, models


class BWChangeSpeed(models.Model):
    _name = 'bwchange.speed'
    _order = 'speed_sequence'

    # General
    name = fields.Char(string="Speed", required=True)
    speed_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('bwchange.speed') or '1000'
        vals['speed_sequence'] = seq
        return super(BWChangeSpeed, self).create(vals)
