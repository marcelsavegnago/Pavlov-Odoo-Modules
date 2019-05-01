# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import api, models


class ServerIntranet(models.Model):
    _name = 'server.intranet'

    @api.multi
    def open_url(self):
        intranet_url = self.env['ir.config_parameter'].sudo().get_param(
            'server.intranet_url', default='')
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': intranet_url}
