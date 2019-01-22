from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Project(models.Model):
    _inherit = 'project.project'

    old_start_date = fields.Date(string='Old Start Date',
                                 help="Used by the Shift Dates function. When the Projects start date changes, the old date is populated in this field then is used when the 'Shift Dates' button is pushed.")

    shift_task_dates = fields.Boolean(string="Shift Task Dates?",
                                      default=True,
                                      help="If checked, when you change the start date of a project, the dates on the Tasks will shift the number of days you change the start date of the Project. If the Project start dates were originally empty, the Start/End dates on the tasks will be set to the Project Start/End Dates unless they were previously set on the Tasks.")

    # SET OLD DATE VALUE WHEN CHANGED *USED FOR DATE SHIFTING
    @api.onchange('date_start')
    def on_change_dates(self):
        if self.old_start_date == False:
            self.old_start_date = self._origin.date_start
        if self.old_start_date == self.date_start:
            self.old_start_date = False

    # SHIFT TASK AND MILESTONE DATES
    def shift_dates(self):
        # ONLY RUN IS SHIFT DATES OPTION IS TRUE
        if self.shift_task_dates and (self.old_start_date != self.date_start):
            original_start_dt = fields.Datetime.from_string(self.old_start_date)
            new_start_dt = fields.Datetime.from_string(self.date_start)
            difference = relativedelta(new_start_dt, original_start_dt)
            years = difference.years
            months = difference.months
            days = difference.days

            # SHIFT TASK DATES
            for record in self.task_ids:
                if record.active and (record.stage_id.is_closed != True):
                    if record.date_start:
                        record.write({'date_start': (record.date_start + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_start': record.project_id.date_start})

                    if record.date_end:
                        record.write({'date_end': (record.date_end + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_end': record.project_id.date})

                    if record.date_deadline:
                        record.write({'date_deadline': (record.date_deadline + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})
                    else:
                        record.write({'date_deadline': record.project_id.date})

            # SHIFT MILESTONE DATES
            if self.use_milestones:
                for record2 in self.milestones:
                    if record2.target_date:
                        record2.write({'target_date': (record2.target_date + relativedelta(years =+ years) + relativedelta(months =+ months) + relativedelta(days =+ days))})

        self.old_start_date = False
