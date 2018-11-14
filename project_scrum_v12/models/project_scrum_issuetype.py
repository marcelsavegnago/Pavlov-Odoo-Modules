from odoo import models, fields, api

class ProjectScrumIssueType(models.Model):
     _name = 'project.scrum_issuetype'
     _order = 'issuetype_sequence'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     issuetype_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_issuetype') or '/'
        vals['issuetype_sequence'] = seq
        return super(ProjectScrumIssueType, self).create(vals)
