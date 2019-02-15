from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    pebbles_key_id = fields.Char(string="Pebbles Key ID")

    @api.multi
    def open_myaccount_url(self,pebbles_key_id):
        return {
        'name'     : 'MyAccount',
        'res_model': 'ir.actions.act_url',
        'type'     : 'ir.actions.act_url',
        'target'   : 'new',
        'url'      : ("https://myaccount.pavlovmedia.net/")
        }

    @api.multi
    def open_createaccount_url(self):
        return {
        'name'     : 'MyAccount',
        'res_model': 'ir.actions.act_url',
        'type'     : 'ir.actions.act_url',
        'target'   : 'new',
        'url'      : "https://myaccount.pavlovmedia.net/"
        }
