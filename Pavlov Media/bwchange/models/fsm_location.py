# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

from odoo import fields, models, api


class FSMLocation(models.Model):
    _inherit = 'fsm.location'

    bwchange_count = fields.Integer(
        compute='_compute_bwchange_count',
        string='# Bandwidth Changes'
    )

    @api.multi
    def _compute_bwchange_count(self):
        for location in self:
            res = self.env['bwchange.change'].search_count(
                [('location_id', '=', location.id)])
            location.bwchange_count = res or 0

    @api.multi
    def action_view_bwchange(self):
        for location in self:
            bwchange_ids = self.env['bwchange.change'].search(
                [('location_id', '=', location.id)])
            action = self.env.ref(
                'bwchange.bwchange_change_action').read()[0]
            action['context'] = {}
            if len(bwchange_ids) > 1:
                action['domain'] = [('id', 'in', bwchange_ids.ids)]
            elif len(bwchange_ids) == 1:
                action['views'] = [(
                    self.env.ref('bwchange.bwchange_change_view__form').id,
                    'form')]
                action['res_id'] = bwchange_ids.ids[0]
            return action
