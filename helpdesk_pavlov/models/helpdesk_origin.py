from odoo import models, fields, api

class HelpdeskOrigin(models.Model):
    _name = 'helpdesk.origin'

#General
    name = fields.Char(string="Origin", required=True)
