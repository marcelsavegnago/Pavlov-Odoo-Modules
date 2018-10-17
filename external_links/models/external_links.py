from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ExternalLink(models.Model):
     _name = 'external_links.link'

#General
     name = fields.Char(string="Name", required=True)
     description = fields.Text(string="Description", required=True)
     url = fields.Char(string="URL", required=True)
     logo = fields.Binary(string="Logo", required=True)
     vpn = fields.Boolean(string="Requires VPN", help="Select if this site/system is only accessable either on the local network or requires VPN access.")
     categories = fields.Many2many('external_links.categories', string="Categories")
     color = fields.Integer(string="Color")

     @api.multi
     def openURL(self,url):
         url = self.url
         return {
          "type": "ir.actions.act_url",
          "url": url,
          "target": "new",
         }
