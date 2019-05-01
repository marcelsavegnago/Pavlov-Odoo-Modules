from odoo import models, fields, api


class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'

    kb_documents = fields.Many2many('ir.attachment', string="KB Documents")

    @api.onchange('tag_ids')
    def on_change_tag_ids(self):
        self.kb_documents = [(6, 0, [])]
        for record in self:
            for i in record.tag_ids:
                record.kb_documents = record.kb_documents + i.documents
