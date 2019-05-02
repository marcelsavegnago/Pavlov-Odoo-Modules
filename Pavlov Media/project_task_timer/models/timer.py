# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import api, fields, models


class Timer(models.Model):
    _name = "timer.timer"

    name = fields.Char()
    active = fields.Boolean(default=True)
    start_timer_date = fields.Datetime()
    end_timer_date = fields.Datetime()
    user_id = fields.Many2one('res.users', string="User")
    task_id = fields.Many2one('project.task', string="Project Task")
    project_id = fields.Many2one('project.project', string="Project")
