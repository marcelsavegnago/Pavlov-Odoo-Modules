from odoo import models, fields, api

class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'

#General
    kb_documents = fields.Many2many('ir.attachment', related="tag_ids.documents", string="KB Documents", store=False)

    #@api.onchange('tag_ids')
    #def _onchange_tag_ids(self):
    #        self.priority = self.ticket_type_id.default_priority
