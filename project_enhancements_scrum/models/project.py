from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

# SCRUM
    next_task_number = fields.Integer(string="Next Task Number",
                                      default="1",
                                      copy=False,
                                      help="Each Project can have it's own task numbers and get added to the Task Label.")
    sprints = fields.Many2many('project.scrum_sprint',
                               relation='project_sprint_rel',
                               column1='project_id',
                               column2='sprint_id',
                               string="Sprints",
                               copy=False)
    use_scrum = fields.Boolean(string="Use scrum",
                               copy=True,
                               context="{'default_use_scrum': use_scrum}")
    releases = fields.One2many('project.scrum_release',
                               'project_id',
                               string="Releases",
                               copy=False)
    epics = fields.One2many('project.scrum_epic',
                            'project_id',
                            string="Epics",
                            copy=True)

    # UPDATE TASK NUMBER LABELS IF THE MAIN LABEL CHANGED
    @api.onchange('label_tasks')
    def on_change_label_tasks(self):
        if self._origin.label_tasks:
            old_label = self._origin.label_tasks
            new_label = self.label_tasks
            for record in self.task_ids:
                new_task_number = record.task_number
                new_task_number = new_task_number.replace(old_label, new_label)
                record.write({'task_number': new_task_number})
