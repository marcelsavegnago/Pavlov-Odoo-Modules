from odoo import models, fields, api

#Main Bandwidth Change Records Model
class ProjectScrumComponents(models.Model):
     _name = 'project.scrum_component'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     component_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_component') or '/'
        vals['component_sequence'] = seq
        return super(ProjectScrumComponents, self).create(vals)
