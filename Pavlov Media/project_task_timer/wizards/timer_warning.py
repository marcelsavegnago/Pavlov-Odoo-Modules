# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

from odoo import _, api, fields, models
from odoo.exceptions import Warning


class TimerWarning(models.TransientModel):
    _name = "timer_warning"

    timer_id = fields.Many2one('timer.timer', string="Running Timer")
    task_id = fields.Many2one('project.task', string="Project Task")

    @api.model
    def default_get(self, default_fields):
        context = self._context
        timer_id = context.get('timer_id')
        task_id = context.get('task_id')
        res = super(TimerWarning, self).default_get(default_fields)
        res.update({'timer_id': timer_id, 'task_id': task_id})
        return res

    @api.multi
    def open_task(self):
        view_id = self.env.ref('project.view_task_form2').id
        if self.task_id:
            return {'view_id': view_id,
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'project.task',
                    'res_id': self.task_id.id,
                    'type': 'ir.actions.act_window',
                    'target': 'current'}
