from odoo import models, fields, api

class LocationHierarchyWizard(models.TransientModel):
    _name = 'fsm.location_hierarchy_wizard'
    _inherits = {'fsm.location': 'location_id'}

    def _get_default_location(self):
        return self.env['fsm_location'].browse(self.env.context.get('active_id'))

    primary_location_id = fields.Many2one('fsm.location', string="Primary Location")
    depth = fields.Selection([
                              ('1', '1 Level'),
                              ('2', '2 Levels'),
                              ('3', '3 Levels'),
                              ('4', '4 Levels')],
                              string="Level Depth",
                              default='1')
    level_1_name = fields.Char(string="Name")
    level_1_spacer = fields.Char(string="Character Spacer")
    level_1_start_num = fields.Integer(string="Start Number",default='1')
    level_1_end_num = fields.Integer(string="End Number",default='1')
    level_1_total = fields.Integer(string="Total",compute="_level_1_total")

    level_2_name = fields.Char(string="Name")
    level_2_spacer = fields.Char(string="Character Spacer")
    level_2_start_num = fields.Integer(string="Start Number",default='1')
    level_2_end_num = fields.Integer(string="End Number",default='1')
    level_2_total = fields.Integer(string="Total",compute="_level_2_total")

    level_3_name = fields.Char(string="Name")
    level_3_spacer = fields.Char(string="Character Spacer")
    level_3_start_num = fields.Integer(string="Start Number",default='1')
    level_3_end_num = fields.Integer(string="End Number",default='1')
    level_3_total = fields.Integer(string="Total",compute="_level_3_total")

    level_4_name = fields.Char(string="Name")
    level_4_spacer = fields.Char(string="Character Spacer")
    level_4_start_num = fields.Integer(string="Start Number",default='1')
    level_4_end_num = fields.Integer(string="End Number",default='1')
    level_4_total = fields.Integer(string="Total",compute="_level_4_total")

    @api.depends('level_1_start_num','level_1_end_num')
    def _level_1_total(self):
        self.level_1_total = self.level_1_end_num - self.level_1_start_num + 1

    @api.depends('level_2_start_num','level_2_end_num')
    def _level_2_total(self):
        self.level_2_total = self.level_2_end_num - self.level_2_start_num + 1

    @api.depends('level_3_start_num','level_3_end_num')
    def _level_3_total(self):
        self.level_3_total = self.level_3_end_num - self.level_3_start_num + 1

    @api.depends('level_4_start_num','level_4_end_num')
    def _level_4_total(self):
        self.level_4_total = self.level_4_end_num - self.level_4_start_num + 1

    @api.multi
    def create_sub_locations(self):
        if self.level_1_name:
            if self.level_1_spacer:
                spacerchar = " " + self.level_1_spacer
            else:
                spacerchar = ""
            for l1 in range(self.level_1_start_num, (self.level_1_end_num + 1)):
                vals = {'partner_id': partner.id,
                        #'owner_id': partner.id,
                        #'customer_id': partner.id,
                        'name': self.level_1_name + spacerchar + str(l1),
                        'owner_id': self.owner_id.id,
                        'customer_id': self.customer_id.id,
                        'parent_id': self.primary_location_id.id}
                new_l1_record = self.env['fsm.location'].create({vals})

                if self.level_2_name:
                    if self.level_2_spacer:
                        spacerchar2 = " " + self.level_1_spacer
                    else:
                        spacerchar2 = ""
                    for l2 in range(self.level_2_start_num, (self.level_2_end_num + 1)):
                        vals = {'name': self.level_1_name + spacerchar2 + str(l1),
                                'owner_id': self.owner_id.id,
                                'customer_id': self.customer_id.id,
                                'parent_id': self.primary_location_id.id}
                        new_l2_record = self.env['fsm.location'].create(vals)

                        if self.level_3_name:
                            if self.level_3_spacer:
                                spacerchar3 = " " + self.level_1_spacer
                            else:
                                spacerchar3 = ""
                            for l3 in range(self.level_2_start_num, (self.level_3_end_num + 1)):
                                vals = {'name': self.level_1_name + spacerchar3 + str(l1),
                                        'owner_id': self.owner_id.id,
                                        'customer_id': self.customer_id.id,
                                        'parent_id': self.primary_location_id.id}
                                new_l3_record = self.env['fsm.location'].create(vals)

                                if self.level_4_name:
                                    if self.level_4_spacer:
                                        spacerchar4 = " " + self.level_1_spacer
                                    else:
                                        spacerchar4 = ""
                                    for l4 in range(self.level_4_start_num, (self.level_4_end_num + 1)):
                                        vals = {'name': self.level_1_name + spacerchar2 + str(l1),
                                                'owner_id': self.owner_id.id,
                                                'customer_id': self.customer_id.id,
                                                'parent_id': self.primary_location_id.id}
                                        new_l4_record = self.env['fsm.location'].create(vals)
