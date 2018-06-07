# -*- coding: utf-8 -*-

from odoo import models, fields

#Main Bandwidth Change Records Model
class partner_floors(models.Model):
     _name = 'pavlov_partnerstructure.floors'

#General
     name = fields.Char(string="Title", required=True)
     account = fields.Many2one('res.partner', string="Account")
     building = fields.Many2one('pavlov_partnerstructure.buildings', string="Building")
