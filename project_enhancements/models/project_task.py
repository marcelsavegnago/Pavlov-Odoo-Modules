from odoo import models, fields, api
from datetime import timedelta

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _order = 'priority desc, date_start, date_end, sequence, date_start, id desc'

    date_start = fields.Datetime(string='Starting Date',
                                 default=fields.Datetime.now,
                                 index=True,
                                 copy=True)
    forecasts = fields.One2many('project.forecast',
                                'task_id',
                                string="Forecasts",
                                help="List of Forecasts related to the Task.")
                                
    # USED IN THE LIST VIEWS ON FORMS
    def open_rec(self):
        return {
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'project.task',
                'res_id': self.id,
                'type': 'ir.actions.act_window',
                'target': 'new',
                'flags': {'form': {'action_buttons': True}}
        }
