from odoo import models, fields

class AgreementType(models.Model):

    _inherit = 'partner_agreement.type'

    circuit_type = fields.Boolean(string="Is Circuit Agreement?", help="When checked, the additional circuit information tab will show on the agreement whenever this type is selected.")
