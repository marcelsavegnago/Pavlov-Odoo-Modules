from odoo import models, fields

class HelpdeskCloseCause(models.Model):
    _name = 'helpdesk.closecause'
    _order = 'name'

#General
    name = fields.Char(string="Name",
                       required=True)
    ticket_type_ids = fields.Many2many('helpdesk.ticket.type',
                                       string="Ticket Types",
                                       required=True)
    actions_taken_ids = fields.Many2many('helpdesk.closeaction',
                                         string="Actions Taken")
    description = fields.Text(string="Description")

    _sql_constraints = [
                        ('field_unique',
                         'unique(name)',
                         'Another Cause has this name. Please update that Ticket Cause.')
                      ]
