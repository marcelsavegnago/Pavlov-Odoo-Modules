# Copyright (C) 2018 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields


class FSMEquipment(models.Model):
    _inherit = 'fsm.equipment'

    node_id = fields.Integer()
