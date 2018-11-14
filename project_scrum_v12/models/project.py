from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    sprints = fields.One2many('project.scrum_sprint', 'id', string="Sprints")
    use_scrum = fields.Boolean(string="Use Scrum")
    release = fields.One2many('project.scrum_release', 'id', string="Releases")
