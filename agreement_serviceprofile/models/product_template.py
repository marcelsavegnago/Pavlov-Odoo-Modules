from odoo import models, fields, api

class Product(models.Model):

    _inherit = 'product.template'

    serviceprofiles = fields.Many2many('agreement_serviceprofile.serviceprofile', string="Service Profiles")
