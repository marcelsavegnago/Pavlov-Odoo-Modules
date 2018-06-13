from odoo import models, fields

#Main Bandwidth Change Records Model
class SalesTerritories(models.Model):
     _name = 'sales_territories.salesterritories'

#General
     name = fields.Char(string="Title", required=True)
     customers = fields.One2many('res.partner', 'salesterritory', string="Customers")
     salespersons = fields.Many2many('res.users', string="Salespersons")
