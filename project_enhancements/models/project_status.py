from odoo import models, fields, api

class ProjectStatus(models.Model):
     _name = 'project.status'

     name = fields.Char(string="Name", required=True)
     description = fields.Char(string="Description")
     status_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.status') or '/'
        vals['status_sequence'] = seq
        return super(ProjectStatus, self).create(vals)
