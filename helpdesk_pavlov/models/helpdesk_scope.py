from odoo import models, fields, api

class HelpdeskScope(models.Model):
    _name = 'helpdesk.scope'
    _order = 'scope_sequence'

#General
    name = fields.Char(string="Scope", required=True)
    scope_sequence = fields.Integer(string="Sequence")
    user_ids = fields.Many2many('res.users', string="Allowed Users", required=True)

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('helpdesk.scope') or '/'
        vals['scope_sequence'] = seq
        return super(HelpdeskScope, self).create(vals)
