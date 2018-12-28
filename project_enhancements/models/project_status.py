from odoo import models, fields, api

class ProjectStatus(models.Model):
     _name = 'project.status'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description", help="Provide a detailed description of the status so users will no when to use this status.")
     status_sequence = fields.Integer(string="Sequence")
     is_closed = fields.Boolean(string="Is Closed Status", help="Specify if this is a closing status. Used by views to help filter out closed items.")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.status') or '/'
        vals['status_sequence'] = seq
        return super(ProjectStatus, self).create(vals)
