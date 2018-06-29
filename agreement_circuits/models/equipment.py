from odoo import models, fields

class Equipment(models.Model):

    _inherit = 'maintenance.equipment'

    customer = fields.Many2one('res.partner', string="Customer")
