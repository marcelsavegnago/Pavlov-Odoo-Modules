# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    myaccount_url = fields.Char(string='MyAccount URL')
    houston_url = fields.Char(string='Houston URL')

    # Functions to fetch MyAccount Configurations
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(myaccount_url=self.env['ir.config_parameter'].sudo().
                   get_param('external_systems.myaccount_url'),
                   houston_url=self.env['ir.config_parameter'].sudo().
                   get_param('external_systems.houston_url'))
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'external_systems.myaccount_url', self.myaccount_url)
        self.env['ir.config_parameter'].sudo().set_param(
            'external_systems.houston_url', self.houston_url)
        return res
