# -*- coding: utf-8 -*-

from odoo import models, fields

#Main Bandwidth Change Records Model
class partner_rooms(models.Model):
     _name = 'pavlov_partnerstructure.rooms'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     unit = fields.Many2one('pavlov_partnerstructure.units', string="Unit")
