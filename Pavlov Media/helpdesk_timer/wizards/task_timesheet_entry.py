# -*- coding: utf-8 -*-
import datetime

from odoo import _, api, fields, models
from odoo.exceptions import Warning


class TaskTimesheetEntry(models.TransientModel):
    _inherit = "task_timesheet_entry"

    ticket_id = fields.Many2one('helpdesk.ticket',
                                string="Ticket",
                                readonly=True)

    @api.model
    def default_get(self, default_fields):
        context = self._context
        starting_date = context.get('start_timer_date')
        ending_date = context.get('end_timer_date')
        diff = datetime.datetime.strptime(
            ending_date, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(
                starting_date, "%Y-%m-%d %H:%M:%S")
        duration = float(diff.days) * 24 + (float(diff.seconds) / 3600)
        rounded_duration = round(duration, 2)
        res = super(TaskTimesheetEntry, self).default_get(default_fields)
        res.update({
            'start_timer_date': starting_date,
            'end_timer_date': ending_date,
            'duration': rounded_duration,
        })
        return res

    @api.multi
    def task_save_entry(self):
        if self.project_id:
            if self.duration == 0.0:
                raise Warning(_("You can't save entry for %s duration") % (
                    self.duration))
            ticket = self.timer_id.ticket_id
            task = self.timer_id.task_id
            vals = {'date': fields.Date.context_today(self),
                    'user_id': self.env.user.id,
                    'name': self.description,
                    'task_id': self.task_id.id,
                    'project_id': self.project_id.id,
                    'unit_amount': self.duration,
                    'account_id': self.project_id.analytic_account_id.id,
                    'helpdesk_ticket_id': ticket.id
                    }
            analytic_line_rec = self.env['account.analytic.line'].create(vals)
            self.ticket_id.write({
                'timesheet_ids': [(4, 0, [analytic_line_rec.id])]})

            self.timer_id.unlink()
            if ticket:
                other_ticket_active_timers = self.env['timer.timer'].search_count([(
                    'ticket_id', '=', ticket.id)])
                if other_ticket_active_timers == 0:
                    ticket.write({'timer_started': False})
            if task:
                other_task_active_timers = self.env['timer.timer'].search_count([(
                    'task_id', '=', task.id)])
                if other_task_active_timers == 0:
                    task.write({'timer_started': False})
        else:
            raise Warning(_("Please link Project to this Task."))

    @api.multi
    def task_discard_entry(self):
        ticket = self.timer_id.ticket_id
        task = self.timer_id.task_id
        self.timer_id.unlink()
        if ticket:
            other_ticket_active_timers = self.env['timer.timer'].search_count(
                [('ticket_id', '=', ticket.id)])
            if other_ticket_active_timers == 0:
                ticket.write({'timer_started': False})
        if task:
            other_task_active_timers = self.env['timer.timer'].search_count(
                [('task_id', '=', task.id)])
            if other_task_active_timers == 0:
                task.write({'timer_started': False})
