from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    story_point_estimate = fields.Many2one('project.scrum_point', string="Story Points")
    fix_versions = fields.Many2many('project.scrum_release', relation='fixedversion_task_rel', column1='task_id', column2='version_id', string="Fix Versions")
    affects_versions = fields.Many2many('project.scrum_release', relation='affectver_task_rel',string="Affects Versions")
    acceptance_criteria = fields.Text(string="Acceptance Criteria")
    categories = fields.Many2many('project.scrum_category', string="Categories")
    blocking_tasks = fields.Many2many('project.task', relation='blocking_tasks_rel', column1='task1', column2='task2',string="Blocking Tasks")
    source = fields.Many2one('project.scrum_source', string="Source")
    issue_type = fields.Many2one('project.scrum_issuetype', string="Issue Type")
    labels = fields.Many2many('project.scrum_label', string="Labels")
    use_scrum = fields.Boolean(string="Use Scrum", related='project_id.use_scrum')

    @api.multi
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

    @api.model
    def _read_group_sprint_ids(self, sprints, domain, order):
        # write the domain
        # - ('id', 'in', sprints.ids): add columns that should be present
        # - OR ('team_ids', '=', team_id) if team_id: add team columns
        search_domain = [('id', 'in', sprints.ids)]
        if self.env.context.get('sprint_id'):
            search_domain = ['|', ('sprint_ids', 'in', self.env.context['sprint_id'])] + search_domain

            return sprints.search(search_domain, order=order)

    sprint_id = fields.Many2one('project.scrum_sprint', string="Sprint", group_expand='_read_group_sprint_ids')
