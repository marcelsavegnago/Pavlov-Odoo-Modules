from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

# SCRUM
    story_point_estimate = fields.Many2one('project.scrum_point', string="Story Points")
    task_number = fields.Char(string="Task Number")
    fix_versions = fields.Many2many('project.scrum_release', relation='fixedversion_task_rel', column1='task_id', column2='version_id', string="Fix Version/s")
    affects_versions = fields.Many2many('project.scrum_release', relation='affectver_task_rel',string="Affects Version/s")
    acceptance_criteria = fields.Text(string="Acceptance Criteria")
    categories = fields.Many2many('project.scrum_category', string="Categories")
    blocking_tasks = fields.Many2many('project.task', relation='blocking_tasks_rel', column1='task1', column2='task2',string="Blocking Tasks")
    source = fields.Many2one('project.scrum_source', string="Source")
    issue_type = fields.Many2one('project.scrum_issuetype', string="Issue Type")
    labels = fields.Many2many('project.scrum_label', string="Labels")
    use_scrum = fields.Boolean(string="Use Scrum", related='project_id.use_scrum')
    issue_type_image = fields.Binary(string="Issue Type Image", related='issue_type.issue_type_image')
    reporter = fields.Many2one('res.user', string="Reporter")

    forecasts = fields.One2many('project.forecast', 'task_id', string="Forecasts")

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

    # USED FOR GROUP BY SPRINTS
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

    # USED TO SET STORY NUMBER (WITH PREFIX) AND UPDATE NEXT NUMBER ON PROJECT
    @api.model
    def create(self, values):
        # Override the original create function for the res.partner model
        record = super(ProjectTask, self).create(values)
        record['task_number'] = record.project_id.label_tasks + '-' + str(record.project_id.next_task_number)
        next_num = record.project_id.next_task_number + 1
        record.project_id.write({'next_task_number': next_num})

        return record

    # UPDATE OR CREATE FORECAST AUTOMATICALLY IF ALL REQUIRED VALUES ARE MET
    @api.onchange('date_start', 'date_end', 'sprint_id', 'planned_hours')
    def on_change_task_forecast(self):
        # If Task already has Forecasts related
        if self.forecasts:
            if self.date_start and self.date_end and self.planned_hours and self.user_id and self.allow_forecast:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then each forecast record can be updated
                if employee_id.id:
                    for record in self.forecasts: # MAYBE NEED and employee.id == employee_id (to only update forecasts related to the assigned user)
                        record.write({'start_date': self.date_start, 'end_date': self.date_end, 'sprint_id': self.sprint_id.id, 'resource_hours': self.planned_hours, 'employee_id': employee_id.id})
        else:
            if self.date_start and self.date_end and self.planned_hours and self.user_id and self.allow_forecast:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then a forecast record can be created...
                if employee_id.id:
                    self.env['project.forecast'].create({'sprint_id': self.sprint_id.id, 'employee_id': employee_id.id, 'project_id': self.project_id.id, 'resource_hours': self.planned_hours, 'task_id': self._origin.id, 'start_date': self.date_start, 'end_date': self.date_end})

# MILESTONES
    milestone_id = fields.Many2one('project.milestone', string="Milestones")
    use_milestones = fields.Boolean(string="Use Milestones", related='project_id.use_milestones')
