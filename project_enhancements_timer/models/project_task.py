from odoo import api, fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    timer_started = fields.Boolean(default=False)
    start_timer_date = fields.Datetime()
    end_timer_date = fields.Datetime()

    @api.multi
    def task_start_timer(self):
        self.write({'timer_started': True,
                    'start_timer_date': fields.Datetime.now()})

    @api.multi
    def task_end_timer(self):
        self.write({'end_timer_date': fields.Datetime.now()})
        context = dict(self.env.context)
        context.update({'start_timer_date': self.start_timer_date, 'end_timer_date': self.end_timer_date,'default_project_id': self.project_id.id, 'default_task_id': self.id})
        view_id = self.env.ref('project_enhancements_timer.timesheet_entry_view_form')
        return {
            'view_id': view_id.ids,
            'view_type': 'form',
            "view_mode": 'form',
            'res_model': 'timesheet_entry',
            'type': 'ir.actions.act_window',
            'context': context,
            'target': 'new'
        }
