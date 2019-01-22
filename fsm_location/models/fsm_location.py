from odoo import models, fields, api

class FSMLocation(models.Model):
    _name = 'fsm.location'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Field Service Location'

    ref = fields.Char(string='Internal Reference')
    direction = fields.Char(string='Directions')
    partner_id = fields.Many2one('res.partner', string='Related Partner',
                                 ondelete='restrict',
                                 delegate=True, auto_join=True)
    owner_id = fields.Many2one('res.partner', string='Related Owner',
                               required=True, ondelete='restrict',
                               auto_join=True)
    customer_id = fields.Many2one('res.partner', string='Billed Customer',
                                  required=True, ondelete='restrict',
                                  auto_join=True)
    contact_id = fields.Many2one('res.partner', string='Primary Contact',
                                 domain="[('is_company', '=', False)]",
                                 index=True)
    description = fields.Char(string='Description')

    parent_id = fields.Many2one('fsm.location', string='Parent')
    notes = fields.Text(string="Notes")
