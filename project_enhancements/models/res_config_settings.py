from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_project_enhancements_date_shifting = fields.Boolean(string="Task Date Shifting")
    module_project_enhancements_milestones = fields.Boolean(string="Miletones")
    module_project_enhancements_templates = fields.Boolean(string="Templates")
    module_project_enhancements_scrum = fields.Boolean(string="Scrum")
#    module_hr_timesheet = fields.Boolean(string="Task Logs")
#    group_subtask_project = fields.Boolean("Sub-tasks", implied_group="project.group_subtask_project")
#    group_project_rating = fields.Boolean("Use Rating on Project", implied_group='project.group_project_rating')
