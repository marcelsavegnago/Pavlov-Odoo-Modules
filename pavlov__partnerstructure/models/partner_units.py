# -*- coding: utf-8 -*-

from odoo import models, fields

#Main Bandwidth Change Records Model
class partner_units(models.Model):
     _name = 'pavlov_partnerstructure.units'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     floor = fields.Many2one('pavlov_partnerstructure.floors', string="Floor")