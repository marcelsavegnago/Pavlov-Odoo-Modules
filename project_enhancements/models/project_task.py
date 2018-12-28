from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _order = 'priority desc, date_start, date_end, sequence, date_start, id desc'

# SCRUM
    story_point_estimate = fields.Many2one('project.scrum_point', string="Story Points", help="Story points are a unit of measure for expressing an estimate of the overall effort that will be required to fully implement a product backlog item or any other piece of work.")
    task_number = fields.Char(string="Task Number", help="Auto populated from the Task Label and Next Task Number, set on the Project")
    fix_versions = fields.Many2many('project.scrum_release', relation='fixedversion_task_rel', column1='task_id', column2='version_id', string="Fix Version/s", help="The 'Fix version' is used to indicate the future version where the issue will be resolved.")
    affects_versions = fields.Many2many('project.scrum_release', relation='affectver_task_rel',string="Affects Version/s", help="The 'Affects version' assigns an issue to a specific version.")
    acceptance_criteria = fields.Text(string="Acceptance Criteria", help="Acceptance Criteria are a set of statements, each with a clear pass/fail result, that specify both functional and non-functional requirements which constitute as the 'Definition of Done'.")
    categories = fields.Many2many('project.scrum_category', string="Categories", help="Categories can help you organize Tasks. Categories are global and can be setup in the Configuration menu.")
    blocking_tasks = fields.Many2many('project.task', relation='blocking_tasks_rel', column1='task1', column2='task2',string="Blocking Tasks", help="Blocking Tasks are linked Tasks that would prevent the current Task from being completed until the linked Task is completed.")
    source = fields.Many2one('project.scrum_source', string="Source", help="The Source specifies where or who the Task originated from.")
    issue_type = fields.Many2one('project.scrum_issuetype', string="Issue Type", help="Use Issue Types to better organize Tasks. Issue Types are global and setup via the Configuration menu.")
    labels = fields.Many2many('project.scrum_label', string="Labels", help="Labels can be used to better organize Tasks. Labels are global and setup via the Configuration menu.")
    use_scrum = fields.Boolean(string="Use Scrum", related='project_id.use_scrum', help="Enable this Project to use scrum. Scrum includes Story Pointing, Versions, Sprints and more.")
    issue_type_image = fields.Binary(string="Issue Type Image", related='issue_type.issue_type_image', help="The Issue Type image shows up on the kanban boards and Task to show a quick visualization of the type of issue.")
    reporter = fields.Many2one('res.user', string="Reporter", help="Whomever reported the Task. Must be a user of the system.")

    date_start = fields.Datetime(copy=True)
    date_end = fields.Datetime(copy=True)
    date_deadline = fields.Date(copy=True)

    forecasts = fields.One2many('project.forecast', 'task_id', string="Forecasts", help="List of Forecasts related to the Task.")
    allow_auto_forecast = fields.Boolean(string="Allow Auto Forecasts", related='project_id.allow_auto_forecast', help="Enables the ability for forecasts to be auto created on the Task. Related to the Project 'Allow Auto Forecasts' setting. Requires the Task to be assigned, start/end dates and planned hours.")

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
        # Only perform this action if the project has 'Allow Auto Forecasts' enabled AND all the forecast required fields are filled in
        if self.allow_auto_forecast and self.date_start and self.date_end and self.planned_hours and self.user_id:
            # If Task already has Forecasts then update them
            if self.forecasts:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then each forecast record can be updated
                if employee_id.id:
                    for record in self.forecasts: # MAYBE NEED and employee.id == employee_id (to only update forecasts related to the assigned user)
                        record.sudo().write({'start_date': self.date_start, 'end_date': self.date_end, 'sprint_id': self.sprint_id.id, 'resource_hours': self.planned_hours, 'employee_id': employee_id.id})

            # If no forecasts exist then create it
            else:
                # Check if there is an employee record associated with the user_id
                employee_id = self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
                # If there is a employee record for the user_id, then a forecast record can be created...
                if employee_id.id:
                    self.env['project.forecast'].sudo().create({'sprint_id': self.sprint_id.id, 'employee_id': employee_id.id, 'project_id': self.project_id.id, 'resource_hours': self.planned_hours, 'task_id': self._origin.id, 'start_date': self.date_start, 'end_date': self.date_end})

# MILESTONES
    milestone_id = fields.Many2one('project.milestone', string="Milestones", help="The Milestone this Task is related to.")
    use_milestones = fields.Boolean(string="Use Milestones", related='project_id.use_milestones', help="If enabled, then Milestones will be available. Related to the Project 'Use Milestones' field.")
