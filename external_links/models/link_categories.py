from odoo import models, fields, api

#Main Bandwidth Change Records Model
class LinkCategories(models.Model):
     _name = 'external_links.categories'

#General
     name = fields.Char(string="Name", required=True)
