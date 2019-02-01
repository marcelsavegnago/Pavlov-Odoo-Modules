from odoo import models, fields, api

class ProjectScrumEpic(models.Model):
     _name = 'project.scrum_epic'
     _order = 'epic_sequence'

#General
     name = fields.Char(string="Title",
                        required=True)
     description = fields.Text(string="Description")
     priority = fields.Selection([
                                  ('highest','Highest'),
                                  ('high','High'),
                                  ('medium','Medium'),
                                  ('low','Low'),
                                  ('lowest','Lowest')],
                                  string="Priority",
                                  required=False)
     progress = fields.Float(string="Progress",
                             compute="_compute_epic_progress",
                             store=True,
                             help="Percentage of Completed Tasks vs Incomplete Tasks.")
     project_id = fields.Many2one('project.project',
                                   string="Project")
     project_tasks = fields.One2many('project.task',
                                     'epic_id',
                                     string="Project Tasks")
     epic_sequence = fields.Integer(string="Sequence")
     fix_versions = fields.Many2many('project.scrum_release',
                                     relation='fixedversion_epic_rel',
                                     column1='epic_id',
                                     column2='version_id',
                                     string="Fix Version/s",
                                     help="The 'Fix version' is used to indicate the future version where the issue will be resolved.")
     affects_versions = fields.Many2many('project.scrum_release',
                                         relation='affectver_epic_rel',
                                         column1='epic_id',
                                         column2='version_id',
                                         string="Affects Version/s",
                                         help="The 'Affects version' assigns an issue to a specific version.")
     labels = fields.Many2many('project.scrum_label',
                               string="Labels",
                               help="Labels can be used to better organize Tasks. Labels are global and setup via the Configuration menu.")
     color = fields.Integer(string='Color Index')

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_epic') or '/'
        vals['epic_sequence'] = seq
        return super(ProjectScrumEpic, self).create(vals)

     # COMPUTE EPIC PROGRESS
     @api.depends('project_tasks.stage_id')
     def _compute_epic_progress(self):
        total_tasks_count = 0.0
        closed_tasks_count = 0.0
        for record in self:
            for task_record in record.project_tasks:
                total_tasks_count += 1
                if (task_record.stage_id.is_closed == True):
                    closed_tasks_count += 1
            if (total_tasks_count > 0):
                record.progress = (closed_tasks_count / total_tasks_count) * 100
            else:
                record.progress = 0.0
