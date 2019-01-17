from odoo import models, fields, api

class ServerPowerBI(models.Model):
     _name = 'server.powerbi'

     @api.multi
     def open_url(self):
        powerbi_url = self.env['ir.config_parameter'].sudo().get_param('server.powerbi_url', default='')
        return {
                 'name'     : 'Go to website',
                 'res_model': 'ir.actions.act_url',
                 'type'     : 'ir.actions.act_url',
                 'target'   : 'new',
                 'url'      : powerbi_url}
