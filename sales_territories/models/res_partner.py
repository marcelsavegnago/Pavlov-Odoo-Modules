from odoo import models, fields
class Partner(models.Model):
    _inherit = 'res.partner'

    salesterritory = fields.Many2one('sales_territories.salesterritories', string="Sales Territory")
