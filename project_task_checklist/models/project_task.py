from odoo import models, fields, api, SUPERUSER_ID


class ProjectTask(models.Model):
    _inherit = 'project.task'

# Checklists
    checklist_ids = fields.One2many('project.task_checklist',
                                    'task_id',
                                    string="Checklists",
                                    copy=True)
    checklist_progress = fields.Float(string="Progress",
                                      compute="_compute_checklist_progress",
                                      help="Percentage of Completed Checklist \
                                      Items vs Incomplete ones.")

    # COMPUTE CHECKLIST PROGRESS
    @api.depends('checklist_ids.is_complete')
    def _compute_checklist_progress(self):
        total_checklist_count = 0.0
        closed_checklist_count = 0.0
        for record in self:
            for checklist_record in record.checklist_ids:
                total_checklist_count += 1
                if checklist_record.is_complete:
                    closed_checklist_count += 1
            if (total_checklist_count > 0):
                record.checklist_progress = (
                    closed_checklist_count / total_checklist_count) * 100
            else:
                record.checklist_progress = 0.0
