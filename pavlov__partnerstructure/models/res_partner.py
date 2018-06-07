from odoo import models, fields, api

class Partner(models.Model):

    _inherit = 'res.partner'

    buildings = fields.One2many('pavlov_partnerstructure.buildings', 'account', string="Buildings")
    floors = fields.One2many('pavlov_partnerstructure.floors', 'account', string="Floors")
    units = fields.One2many('pavlov_partnerstructure.units', 'account', string="Units")
    rooms = fields.One2many('pavlov_partnerstructure.rooms', 'account', string="Rooms")
