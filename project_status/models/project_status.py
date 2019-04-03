from odoo import models, fields, api

class ProjectStatus(models.Model):
     _name = 'project.status'
     _order = 'status_sequence'

     name = fields.Char(string="Name",
                        required=True)
     description = fields.Char(string="Description")
     status_sequence = fields.Integer(string="Sequence")
     is_closed = fields.Boolean(string="Is Closed Status",
                                help="Specify if this is a closing status. Used by views to help filter out closed items.")
     fold = fields.Boolean(string="Folded")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.status') or '/'
        vals['status_sequence'] = seq
        return super(ProjectStatus, self).create(vals)
