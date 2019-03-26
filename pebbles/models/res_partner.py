from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    external_systems_flag = fields.Boolean(string="External System?")
    external_systems_id = fields.Char(string="External System ID")
