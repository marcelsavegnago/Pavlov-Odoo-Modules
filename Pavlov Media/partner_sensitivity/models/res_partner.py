from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    sensitivity_id = fields.Many2one('partner.sensitivity',
                                     string="Sensitivity")
