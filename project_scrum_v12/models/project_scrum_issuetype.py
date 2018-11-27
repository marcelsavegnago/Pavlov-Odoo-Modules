from odoo import models, fields, api

class ProjectScrumIssueType(models.Model):
     _name = 'project.scrum_issuetype'
     _order = 'issuetype_sequence'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     issuetype_sequence = fields.Integer(string="Sequence")
     color = fields.Integer(string='Color Index')
     issue_type_image = fields.Binary(string="Issue Type Image")

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_issuetype') or '/'
        vals['issuetype_sequence'] = seq
        return super(ProjectScrumIssueType, self).create(vals)
