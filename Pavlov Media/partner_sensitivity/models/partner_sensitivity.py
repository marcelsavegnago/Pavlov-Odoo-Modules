from odoo import models, fields, api


class PartnerSensitivity(models.Model):
    _name = 'partner.sensitivity'
    _order = 'sequence'
    _description = 'Partner Sensitivity Level'

    name = fields.Char(string="Sensitivity Level", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer(string="Sequence")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code(
            'res_partner.sensitivity') or 0
        vals['sequence'] = seq
        return super(PartnerSensitivity, self).create(vals)
