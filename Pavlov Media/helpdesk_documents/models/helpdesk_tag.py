# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import models, fields, api


class HelpdeskTag(models.Model):
    _inherit = 'helpdesk.tag'

    documents = fields.Many2many('ir.attachment', string="KB Documents")
    documents_folder = fields.Many2one('documents.folder',
                                       string="KB Documents Folder")
