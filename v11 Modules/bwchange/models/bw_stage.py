from odoo import models, fields, api

class BWChangeStage(models.Model):
    _name = 'bwchange.stage'
    _order = 'stage_sequence'

    #General
    name = fields.Char(string="Stage", required=True)
    stage_sequence = fields.Integer(string="Sequence")
    description = fields.Text(string="Description")
    default_state = fields.Selection([
                                     ('draft', 'Draft'),
                                     ('active', 'Active'),
                                     ('inactive', 'Inactive')],
                                     string="Default State")
    fold = fields.Boolean(string="Folded")
    is_close = fields.Boolean(string="Closing Kanban Stage")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('bwchange.stage') or '/'
        vals['stage_sequence'] = seq
        return super(BWChangeStage, self).create(vals)
