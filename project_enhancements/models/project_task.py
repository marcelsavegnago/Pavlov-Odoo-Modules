from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _order = 'priority desc, date_start, date_end, sequence, date_start, id desc'

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
