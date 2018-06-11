from odoo import models, fields

#Main Bandwidth Change Records Model
class partner_units(models.Model):
     _name = 'pavlov_partnerstructure.units'
     _inherit = 'pavlov_partnerstructure.floors'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     floor = fields.Many2one('pavlov_partnerstructure.floors', string="Floor")
     building = fields.Many2one('pavlov_partnerstructure.buildings', related='floor.building', string="Building", readonly=True)
