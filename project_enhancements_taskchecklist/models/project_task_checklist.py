from odoo import models, fields, api

class ProjectTaskChecklist(models.Model):
     _name = 'project.task_checklist'
     _order = 'checklist_sequence'

#General
     name = fields.Char(string="Title",
                        required=True)
     description = fields.Text(string="Description")
     is_complete = fields.Boolean(string="Completed")
     task_id = fields.Many2one('project.task',
                                string="Task")
     checklist_sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.task_checklist') or '/'
        vals['sequence'] = seq
        return super(ProjectTaskChecklist, self).create(vals)
