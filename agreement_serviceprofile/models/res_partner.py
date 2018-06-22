from odoo import models, fields, api

class Partner(models.Model):

    _inherit = 'res.partner'

    serviceprofiles = fields.One2many('agreement_serviceprofile.serviceprofile', 'name', string="Service Profiles")
