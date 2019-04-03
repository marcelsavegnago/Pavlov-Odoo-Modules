from odoo import models, fields

class Project(models.Model):
    _inherit = 'project.project'

# PAVLOV MEDIA SPECIFIC FIELDS
    project_summary = fields.Text(string="Project Summary")
    early_services_date = fields.Date(string="Early Services Live",
                                      index=True,
                                      copy=False)
    contract_live_date_data = fields.Date(string="Contract Live Data",
                                          index=True,
                                          copy=False)
    contract_live_date_video = fields.Date(string="Contract Live Video",
                                           index=True,
                                           copy=False)
    contract_end_date_data = fields.Date(string="Contract End Data",
                                         index=True,
                                         copy=False)
    contract_end_date_video = fields.Date(string="Contract End Video",
                                          index=True,
                                          copy=False)
    tag_ids = fields.Many2many('project.tags', string="Tags")
    construction_manager = fields.Many2one('res.users',
                                           string="Construction Manager")
