# Copyright (C) 2018 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    type = fields.Selection([('installation', 'Installation'),
                             ('maintenance', 'Maintenance'),
                             ('investigate', 'Investigate'),
                             ('repair', 'Repair'),
                             ('rma', 'RMA'),
                             ('decommission', 'Decommission')],
                            string='Type', required=True)
