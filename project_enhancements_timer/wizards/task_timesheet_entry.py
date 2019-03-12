import datetime

from odoo import _, api, fields, models
from odoo.exceptions import Warning

class TaskTimesheetEntry(models.TransientModel):
    _name = "task_timesheet_entry"

    start_timer_date = fields.Datetime(string="Start Date", readonly=True)
    end_timer_date = fields.Datetime(string="End Date", readonly=True)
    description = fields.Char(string="Description", required=True, default="Time Worked on Task")
    duration = fields.Float('Duration', readonly=False)
    project_id = fields.Many2one('project.project', string="Project", readonly=True)
    task_id = fields.Many2one('project.task', string="Task", readonly=True)
    timer_id = fields.Many2one('timer.timer', string="Timer")

    @api.model
    def default_get(self, default_fields):
        context = self._context
        starting_date = context.get('start_timer_date')
        ending_date = context.get('end_timer_date')
        diff = datetime.datetime.strptime(
            ending_date, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(starting_date, "%Y-%m-%d %H:%M:%S")
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
                raise Warning(_("You can't save entry with %s duration") % (self.duration))
            vals = {'date': fields.Date.context_today(self),
                    'user_id': self.env.user.id,
                    'name': self.description,
                    'task_id': self.task_id.id,
                    'project_id': self.project_id.id,
                    'unit_amount': self.duration,
                    'account_id': self.project_id.analytic_account_id.id
                    }
            analytic_line_rec = self.env['account.analytic.line'].create(vals)
            self.task_id.write({'timesheet_ids': [(4, 0, [analytic_line_rec.id])]})
            self.timer_id.unlink()
            other_active_timers = self.env['timer.timer'].search_count([('task_id','=',self.task_id.id)])
            if other_active_timers == 0:
                self.task_id.write({'timer_started': False})
        else:
            raise Warning(_("Please link Project to this Task to save the entry"))

    @api.multi
    def task_discard_entry(self):
        self.timer_id.unlink()
        other_active_timers = self.env['timer.timer'].search_count([('task_id','=',self.task_id.id)])
        if other_active_timers == 0:
            self.task_id.write({'timer_started': False})
