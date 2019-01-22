from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

# MILESTONES
    milestones = fields.One2many('project.milestone', 'project_id',
                                 string="Milestones",
                                 copy=True)
    use_milestones = fields.Boolean(string="Use Milestones",
                                    copy=True)
