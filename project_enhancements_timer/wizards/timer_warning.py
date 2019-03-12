from odoo import _, api, fields, models
from odoo.exceptions import Warning

class TimerWarning(models.TransientModel):
    _name = "timer_warning"

    timer_id = fields.Many2one('timer.timer', string="Running Timer")

    @api.model
    def default_get(self, default_fields):
        context = self._context
        timer_id = context.get('timer_id')
        res = super(TimerWarning, self).default_get(default_fields)
        res.update({'timer_id': timer_id})
        return res
