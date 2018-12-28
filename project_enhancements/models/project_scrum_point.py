from odoo import models, fields, api

class ProjectScrumPoint(models.Model):
     _name = 'project.scrum_point'
     _order = 'point_sequence'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description", help="Describe what the pointing means to help assist users.")
     point_sequence = fields.Integer(string="Sequence")
     point_value = fields.Integer(string="Value", help="Integer value of the scrum point, to be used with compute functions")
     color = fields.Integer(string='Color Index')

     _sql_constraints = [
         ('name_uniq', 'unique (name)', "Tag name already exists!"),
     ]

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.scrum_point') or '/'
        vals['point_sequence'] = seq
        return super(ProjectScrumPoint, self).create(vals)
