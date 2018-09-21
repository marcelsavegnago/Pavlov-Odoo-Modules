from odoo import models, fields, api

class HelpdeskTopic(models.Model):
    _name = 'helpdesk.topic'

#General
    name = fields.Char(string="Topic", required=True)
