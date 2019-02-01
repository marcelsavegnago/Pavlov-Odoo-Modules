from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    sample_field = fields.Char(string="Sample")
