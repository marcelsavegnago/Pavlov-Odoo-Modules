# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    intranet_url = fields.Char(string='Intranet URL')

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(intranet_url=self.env['ir.config_parameter'].sudo().
                   get_param('server.intranet_url'))
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('server.intranet_url',
                                                         self.intranet_url)
        return res
