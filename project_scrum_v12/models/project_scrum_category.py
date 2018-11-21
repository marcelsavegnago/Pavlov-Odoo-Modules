from odoo import models, fields, api

class ProjectScrumCategory(models.Model):
     _name = 'project.scrum_category'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     category_sequence = fields.Integer(string="Sequence")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_category') or '/'
        vals['category_sequence'] = seq
        return super(ProjectScrumCategory, self).create(vals)
