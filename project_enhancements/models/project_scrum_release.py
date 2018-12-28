from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class ProjectScrumRelease(models.Model):
     _name = 'project.scrum_release'

     name = fields.Char(string="Release Name", required=True)
     description = fields.Text(string="Description", help="Provides and area for text describing the release.")
     release_date = fields.Date(string="Release Date", help="The official date the release was put into production.")
     project_tasks = fields.Many2many('project.task', relation='fixedversion_task_rel', column1='version_id', column2='task_id', string="Project Tasks", help="List the completed Project Tasks that were included in the Release.")
     status = fields.Selection([('unreleased','Unreleased'),('released','Released')], string="status", default="unreleased")
     release_notes = fields.Text(string="Release Notes", help="Auto populates when the release is completed using the Tasks. If text exists, the auto populated notes get appended to this field.")
     project_id = fields.Many2one('project.project', string="Project", required=True)
     color = fields.Integer(string='Color Index')

     @api.multi
     def release_version_and_new(self):
         version_start = date.today()
         self.release_date = date.today()
         project = self.project_id
         self.color = 10
         new_version = self.env['project.scrum_release'].create({'name': "new", 'color': 4, 'project_id': self.project_id.id})

         if self.release_notes:
             notes = self.release_notes + "\n" + self.name + " Release Notes"
         else:
             notes = self.name + " Release Notes"

         for record in self.project_tasks:
             if record.stage_id.is_closed == False:
                record.fix_versions = new_version
             else:
                    notes = notes + "\n" + "  (" + record.issue_type.name + ") " + record.name

         self.release_notes = notes
         self.status = 'released'

         return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.scrum_release',
            'target': 'current',
            'res_id': new_version.id,
            'type': 'ir.actions.act_window'
         }
