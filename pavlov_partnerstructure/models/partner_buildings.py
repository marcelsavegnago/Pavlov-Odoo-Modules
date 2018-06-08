from odoo import models, fields, api

#Main Bandwidth Change Records Model
class partner_buildings(models.Model):
     _name = 'pavlov_partnerstructure.buildings'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
