from odoo import models, fields, api

class ProjectScrumSource(models.Model):
     _name = 'project.scrum_source'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description", help="Provide a description of the Source to help users.")
     source_sequence = fields.Integer(string="Sequence")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_source') or '/'
        vals['source_sequence'] = seq
        return super(ProjectScrumSource, self).create(vals)
