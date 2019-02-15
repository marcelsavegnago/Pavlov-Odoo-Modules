from odoo import models, fields

class HelpdeskCloseAction(models.Model):
    _name = 'helpdesk.closeaction'
    _order = 'name'

#General
    name = fields.Char(string="Name",
                       required=True)
    cause_ids = fields.Many2many('helpdesk.closecause',
                                 string="Causes",
                                 required=True)
    description = fields.Text(string="Description")
    info_required = fields.Boolean(string="More Information Required",
                                   help="Select if it's required for the user to enter more information when this action is used.")

    _sql_constraints = [
                        ('field_unique',
                         'unique(name)',
                         'Another Action Taken has this name. Please update that Ticket Action Taken.')
                      ]
