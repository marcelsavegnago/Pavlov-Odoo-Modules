from odoo import models, fields, api

class ProjectScrumLabel(models.Model):
     _name = 'project.scrum_label'
     _order = 'label_sequence'

     name = fields.Char(string="Name",
                        required=True)
     description = fields.Char(string="Description")
     label_sequence = fields.Integer(string="Sequence")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_label') or '/'
        vals['label_sequence'] = seq
        return super(ProjectScrumLabel, self).create(vals)
