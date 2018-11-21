from odoo import models, fields, api

class ReportServerPowerBI(models.Model):
     _name = 'reportserver.powerbi'
#     _inherit="base.config.settings"

     powerbi_url = fields.Char(string="Power BI Report Server URL")

#    my_setting = fields.Char(string='My Setting')

#    def get_values(self):
#        res = super(ResConfigSettings, self).get_values()
#        res.update(
#            my_setting=self.env['ir.config_parameter'].sudo().get_param('openacademy.my_setting')
#        )
#        return res

#    def set_values(self):
#        super(ResConfigSettings, self).set_values()
#        self.env['ir.config_parameter'].sudo().set_param('openacademy.my_setting', self.my_setting)
