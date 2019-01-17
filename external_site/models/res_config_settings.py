from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    external_site_url = fields.Char(string='External Site URL')
    external_sites = field.One2many('external.site', 'id', string="")

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            external_site_url=self.env['ir.config_parameter'].sudo().get_param('external_site.external_site_url')
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('external_site.external_site_url', self.external_site_url)
