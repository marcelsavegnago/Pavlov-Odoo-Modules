from odoo import models, fields, api

class HelpdeskTag(models.Model):
    _inherit = 'helpdesk.tag'

#General
    documents = fields.Many2many('ir.attachment', string="KB Documents")
    documents_folder = fields.Many2one('documents.folder', string="KB Documents Folder")
