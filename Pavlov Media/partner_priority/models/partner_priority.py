# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PartnerPriority(models.Model):
    _name = 'partner.priority'
    _order = 'sequence'
    _description = 'Partner Priority'

    name = fields.Char(string="Priority", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code(
            'res_partner.priority') or 0
        vals['sequence'] = seq
        return super(PartnerPriority, self).create(vals)
