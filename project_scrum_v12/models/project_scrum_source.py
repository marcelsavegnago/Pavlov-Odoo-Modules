from odoo import models, fields, api

class ProjectScrumSource(models.Model):
     _name = 'project.scrum_source'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     source_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_source') or '/'
        vals['source_sequence'] = seq
        return super(ProjectScrumSource, self).create(vals)
