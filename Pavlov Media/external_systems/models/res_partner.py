# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    external_systems_flag = fields.Boolean(
      string='External Systems Flag')
    external_systems_id = fields.Char(string="External Systems ID")
    owned_by = fields.Selection(
      [('pebbles', 'Pebbles'),
       ('fttx', 'FTTX'),
       ('odoo', 'Odoo')],
      string="Owned By")

    # Clear Fields if External System Flag is unchecked
    @api.onchange('external_systems_flag')
    def on_change_external_systems_flag(self):
        if not self.external_systems_flag:
            self.owned_by = False
            self.external_systems_id = False
        if (self.external_systems_flag) and (self.owned_by is not True):
            self.owned_by = 'pebbles'

    # Open the Mimic MyAccount URL linked to partner record
    @api.multi
    def open_mimic_myaccount(self, external_systems_id):
        myaccount_url = self.env['ir.config_parameter'].sudo().get_param(
            'external_systems.myaccount_url', default='')
        return {
            'name': 'MyAccount',
            'res_model': 'ir.actions.act_url',
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': (myaccount_url + "/mimic/" + self.external_systems_id)
        }
