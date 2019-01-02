from odoo import models, fields, api

class ProjectType(models.Model):
     _name = 'project.type'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description", help="Provide a detailed description of the project type so users will no when to use this status.")
     type_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.type') or '/'
        vals['type_sequence'] = seq
        return super(ProjectType, self).create(vals)
