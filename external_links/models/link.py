from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ExternalLink(models.Model):
     _name = 'external.link'

#General
     name = fields.Char(string="Name", required=True)
     url = fields.Char(string="URL", required=True)
