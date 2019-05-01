# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    bandwidth_changes = fields.One2many('bwchange.change',
                                        'partner_id',
                                        string="Bandwidth Changes")
