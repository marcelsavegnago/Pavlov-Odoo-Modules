# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    external_systems_flag = fields.Boolean(
      default=False, string='External Systems Flag')
    external_systems_id = fields.Char(string="External Systems ID")
    owned_by = fields.Selection([
      ('pebbles', 'Pebbles'), ('fttx', 'FTTX'), ('odoo', 'Odoo')],
      string="Owned By")

    # Clear Fields if External System Flag is unchecked
    @api.onchange('external_systems_flag')
    def on_change_external_systems_flag(self):
        if not self.external_systems_flag:
            self.owned_by = False
            self.external_systems_id = False
        if (self.external_systems_flag) and (self.owned_by is not True):
            self.owned_by = 'odoo'

    # Open the Product in Houston
    @api.multi
    def open_product_in_houston(self, external_systems_id):
        houston_url = self.env['ir.config_parameter'].sudo().get_param(
            'external_systems.houston_url', default='')
        return {
            'name': 'Houston',
            'res_model': 'ir.actions.act_url',
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': (houston_url + "/" + self.external_systems_id)
        }
