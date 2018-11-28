from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    sprints = fields.Many2many('project.scrum_sprint', relation='project_sprint_rel', column1='project_id', column2='sprint_id', string="Sprints", copy=False)
    use_scrum = fields.Boolean(string="Use Scrum")
    releases = fields.One2many('project.scrum_release', 'project_id', string="Releases", copy=False)
    next_task_number = fields.Integer(string="Next Task Number", default="1", copy=False)
