from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    milestone_id = fields.Many2one('project.milestone', string="Milestones")
    use_milestones = fields.Boolean(string="Use Milestones", related='project_id.use_milestones')
