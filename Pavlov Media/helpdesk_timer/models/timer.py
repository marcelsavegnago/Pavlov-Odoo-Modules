# Copyright (C) 2018 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import api, fields, models


class Timer(models.Model):
    _inherit = "timer.timer"

    ticket_id = fields.Many2one('helpdesk.ticket', string="Ticket")
