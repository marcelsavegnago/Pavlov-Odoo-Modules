# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import models, fields


class HelpdeskTicket (models.Model):
    _inherit = 'helpdesk.ticket'

    partner_mobile = fields.Char(string="Mobile", related='partner_id.mobile')

    partner_category_id = fields.Many2many('res.partner.category',
                                           string="Contact Tags",
                                           related='partner_id.category_id')
    linked_nodes = fields.Text()
