# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    powerbi_url = fields.Char(string='PowerBI URL')

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(powerbi_url=self.env['ir.config_parameter'].sudo().
                   get_param('server.powerbi_url'))
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('server.powerbi_url',
                                                         self.powerbi_url)
        return res
