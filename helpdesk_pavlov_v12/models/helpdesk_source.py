from odoo import models, fields, api

class HelpdeskSource(models.Model):
    _name = 'helpdesk.source'
    _order = 'source_sequence'

#General
    name = fields.Char(string="Source", required=True)
    source_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('helpdesk.source') or '/'
        vals['source_sequence'] = seq
        return super(HelpdeskSource, self).create(vals)
