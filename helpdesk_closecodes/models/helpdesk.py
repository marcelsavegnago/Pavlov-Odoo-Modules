from odoo import models, fields, api

class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'

#General
    cause_id = fields.Many2one('helpdesk.closecause',
                               string="Cause")
    action_taken_id = fields.Many2one('helpdesk.closeaction',
                                      string="Action Taken")
    more_info = fields.Text(string="More Information")
    related_info_required = fields.Boolean(string="Action Taken More Info Needed",
                                           related='action_taken_id.info_required')
    related_enable_closecodes = fields.Boolean(string="Close Code Enabled",
                                               related='ticket_type_id.enable_closecode')

    # CLEAR CAUSE AND ACTION TAKEN IF TICKET TYPE CHANGES
    @api.onchange('ticket_type_id')
    def on_change_ticket_type_id(self):
        if self.cause_id:
            self.cause_id = False
        if self.action_taken_id:
            self.action_taken_id = False

    # CLEAR ACTION TAKEN IF CAUSE CHANGES
    @api.onchange('cause_id')
    def on_change_cause_id(self):
        if self.action_taken_id:
            self.action_taken_id = False
