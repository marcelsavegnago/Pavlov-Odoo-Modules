from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

# MILESTONES
    milestone_id = fields.Many2one('project.milestone',
                                   string="Milestones",
                                   help="The Milestone this Task is related to.")
    use_milestones = fields.Boolean(string="Use Milestones",
                                    related='project_id.use_milestones',
                                    help="If enabled, then Milestones will be available. Related to the Project 'Use Milestones' field.")
