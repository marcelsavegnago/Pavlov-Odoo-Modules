from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    allow_auto_forecast = fields.Boolean(string="Allow auto forecasts",
                                         help="Enables the ability for forecasts to be auto created on Project Tasks. Requires the Task to be assigned, start/end dates and planned hours.")

    # SET AUTO FORECAST FIELD FALSE IF ALLOW FORECAST CHANGES TO FALSE
    @api.onchange('allow_forecast')
    def on_change_allow_auto_forecast(self):
        if self.allow_forecast == False:
            self.allow_auto_forecast = False
