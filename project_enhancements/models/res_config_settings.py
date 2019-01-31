from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_project_enhancements_date_shifting = fields.Boolean(string="Task Date Shifting")
    module_project_enhancements_milestones = fields.Boolean(string="Milestones")
    module_project_enhancements_templates = fields.Boolean(string="Templates")
    module_project_enhancements_scrum = fields.Boolean(string="Scrum")
    module_project_enhancements_types = fields.Boolean(string="Types")
    module_project_enhancements_statuses = fields.Boolean(string="Statuses")
    module_project_enhancements_departments = fields.Boolean(string="Department")
    module_project_enhancements_autoforecast = fields.Boolean(string="Auto Forecasts")
