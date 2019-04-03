from odoo import _, api, fields, models
from odoo.exceptions import Warning

class TimerWarning(models.TransientModel):
    _inherit = "timer_warning"

    ticket_id = fields.Many2one('helpdesk.ticket', string="Ticket")

    @api.model
    def default_get(self, default_fields):
        context = self._context
        timer_id = context.get('timer_id')
        task_id = context.get('task_id')
        ticket_id = context.get('ticket_id')
        res = super(TimerWarning, self).default_get(default_fields)
        res.update({'timer_id': timer_id,
                    'task_id': task_id,
                    'ticket_id':ticket_id})
        return res

    @api.multi
    def open_ticket(self):
        view_id = self.env.ref('helpdesk.helpdesk_ticket_view_form').id
        if self.ticket_id:
            return {'view_id': view_id,
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'helpdesk.ticket',
                    'res_id': self.ticket_id.id,
                    'type': 'ir.actions.act_window',
                    'target': 'current'}
