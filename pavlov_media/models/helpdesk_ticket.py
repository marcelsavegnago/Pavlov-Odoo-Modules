from odoo import models, fields, api

class HelpdeskTicket (models.Model):
    _inherit = 'helpdesk.ticket'

    partner_phone = fields.Char(string="Phone", related='partner_id.phone')
    partner_mobile = fields.Char(string="Mobile", related='partner_id.mobile')
    partner_unit = fields.Many2one('fsm.location',
                                   string="Unit",
                                   related='partner_id.service_location_unit_id')
    partner_category_id = fields.Many2many('res.partner.category',
                                           string="Contact Tags",
                                           related='partner_id.category_id')
