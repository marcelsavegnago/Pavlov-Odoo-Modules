from odoo import models, fields

class EquipmentPanel(models.Model):
    _name = 'equipment.panel'

    name = fields.Char(string="Panel ID", required=True)
    aka = fields.Char(string="Aka")
    status = fields.Many2one('equipment.status', string="Status")
    role = fields.Many2one('equipment.role', string="Role")
    type = fields.Many2one('equipment.paneltype', string="Type")
    port_count = fields.Integer(string="Port Count")
    nomenclature = fields.Selection([('bidirectional', 'Bidirectional'),('free_form', 'Free Form'),('odds_evens', 'Odds and Evens'),('range', 'Range'),('vertical', 'Vertical')], string="Nomenclature")
    rows_of_ports = fields.Integer(string="Rows of Ports")
    manufacturer = fields.Many2one('res.partner', string="Manufacturer")
    width = fields.Char(string="Width")
    rack = fields.Many2one('equipment.rack', string="Rack")
    site = fields.Many2one('res.partner', string="Site")
    location = fields.Char(string="Location")
    installed = fields.Boolean(string="Installed")
    notes = fields.Text(string="Notes")
    ru_size = fields.Integer(string="RU Size")
    is_carrier_panel = fields.Boolean(string="Is Carrier Panel?")
