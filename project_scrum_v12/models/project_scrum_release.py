from odoo import models, fields, api

class ProjectScrumRelease(models.Model):
     _name = 'project.scrum_release'

     name = fields.Char(string="Team Name", required=True)
     description = fields.Text(string="Description")
     start_date = fields.Date(string="Start Date")
     release_date = fields.Date(string="Release Date")
     project_tasks = fields.One2many('project.project_task', 'id', string="Project Tasks")
     status = fields.Selection([('unreleased','Unreleased'),('released','Released')], string="status")
     progress = fields.Integer(string="Progres")
     release_notes = fields.Text(string="Release Notes")
     project_id = fields.Many2one('project.project', string="Project")
