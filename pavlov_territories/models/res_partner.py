from odoo import models, fields, api

class Partner(models.Model):

    _inherit = 'res.partner'

    buildings = fields.One2many('pavlov_partnerstructure.buildings', 'account', string="Buildings")
    floors = fields.One2many('pavlov_partnerstructure.floors', 'account', string="Floors")
    units = fields.One2many('pavlov_partnerstructure.units', 'account', string="Units")
    contacts_building = fields.Many2one('pavlov_partnerstructure.buildings', string="Building")
    contacts_floor = fields.Many2one('pavlov_partnerstructure.floors', string="Floor")
    contacts_unit = fields.Many2one('pavlov_partnerstructure.units', string="Unit")
    contacts_room = fields.Char()
