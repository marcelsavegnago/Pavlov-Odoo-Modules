from odoo import models, fields, api

class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'

    #General
    myaccount_id = fields.Char(string="MyAccount ID")

    @api.multi
    def open_myaccount_url(self,myaccount_id):
        return {
        'name'     : 'MyAccount',
        'res_model': 'ir.actions.act_url',
        'type'     : 'ir.actions.act_url',
        'target'   : 'new',
        'url'      : "https://myaccount.pavlovmedia.net"
        }
