# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Priority',
    'summary': "Adds priority to partners.",
    'author': "Patrick Wilson, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/partner-contact",
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base',
                'contacts',
                ],
    'data': [
        'views/res_partner.xml',
        'views/partner_priority.xml',
        'security/ir.model.access.csv',
        'data/partner_priority_data.xml',
    ],
    'development_status': 'Beta',
    'maintainers': ['patrickrwilson'],
}
