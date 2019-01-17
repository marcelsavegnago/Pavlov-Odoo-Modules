from odoo import models, fields, api

class ExternalSite(models.Model):
    _name = 'external.site'

    name = fields.Char(string="Name",
                       required=True)
    description = fields.Text(string="Description")
    image = fields.Binary(string="Menu Image")
    url = fields.Char(string="URL",
                      required=True)
    action = fields.Many2one('ir.actions.actions',
                             string="URL Action")
    menuitem = fields.Many2one('ir.ui.menu',
                               string="Menu Item")
    access_groups = fields.Many2one('res.groups',
                                    string="Access Group",
                                    required=True)
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
    ]

    # USED TO CREATE THE ACTION AND MENUITEM
    @api.model
    def create(self, values):
        for record in self:
            new_action = record.env['ir.actions.act_url'].create({'type': "ir.actions.act_url", 'name': "test",'url': "https://www.google.com",'target': "new"})
            record.action = new_action
        return self
            #record.action = new_action
    #    new_menuitem = self.env['ir.ui.menu'].create({'name': "test",
    #                                                  'web_icon': "external_site,static/description/icon.png",
    #                                                  'action': new_action.id})
