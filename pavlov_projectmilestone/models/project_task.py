from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def _read_group_milestone_ids(self,milestone,domain,order):
        milestone_ids = self.env['pavlov_projectmilestone.milestones'].search([('projects', '=', self.env.context['default_project_id'])])
        return milestone_ids

    milestone = fields.Many2one('pavlov_projectmilestone.milestones', string="Milestones", group_expand='_read_group_milestone_ids')
