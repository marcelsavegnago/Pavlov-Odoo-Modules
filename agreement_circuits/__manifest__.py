# -*- coding: utf-8 -*-
{
    'name': "Partner Agreements Circuit Enhancements",

    'summary': """
        Partner Agreements Circuit Enhancements""",

    'description': """
        This module adds Circuit information to the Partner Agreement Module.

        Requires:
        - Sales
        - Partner Agreements
        - Maintenance (Equipment)
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Agreements',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'partner_agreement', 'sale_management', 'maintenance'],

    # always loaded
    'data': [
        'views/agreement.xml',
        'views/agreement_type.xml',
        'views/circuit_segment.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
