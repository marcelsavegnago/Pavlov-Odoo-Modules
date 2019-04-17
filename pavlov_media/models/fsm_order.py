# Copyright (C) 2018 - TODAY, Open Source Integrators
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields
from odoo.addons.base_geoengine import geo_model


class FSMOrder(geo_model.GeoModel):
    _inherit = 'fsm.order'

    type = fields.Selection([('installation', 'Installation'),
                             ('maintenance', 'Maintenance'),
                             ('investigate', 'Investigate'),
                             ('repair', 'Repair'),
                             ('rma', 'RMA'),
                             ('decommission', 'Decommission')],
                            string='Type', required=True)
