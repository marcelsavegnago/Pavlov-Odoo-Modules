from odoo import models, fields, api

class Partner(models.Model):

    _inherit = 'res.partner'

    bandwidth_changes = fields.One2many('pavlov_bwchange.change', 'account', string="Bandwidth Changes")
