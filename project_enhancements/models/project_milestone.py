from odoo import models, fields, api

class ProjectMilestone(models.Model):
     _name = 'project.milestone'
     _order = 'sequence'

#General
     name = fields.Char(string="Title", required=True)
     target_date = fields.Date(string="Target Date", required=False)
     actual_date = fields.Date(string="Actual Date", required=False)
     percent_complete = fields.Integer(string="Percent Complete")

     project_id = fields.Many2one('project.project', string="Project")
     project_tasks = fields.One2many('project.task', 'milestone_id', string="Project Tasks")
     fold = fields.Boolean(string="KanBan Folded?")
     sequence = fields.Integer(string="Sequence")

     @api.model
     def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('project.milestone') or '/'
        vals['sequence'] = seq
        return super(ProjectMilestone, self).create(vals)
