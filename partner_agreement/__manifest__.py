# -*- coding: utf-8 -*-
{
    'name': "Partner Agreements",

    'summary': """
        Partner Agreements""",

    'description': """
        This module adds Agreements to the partner model.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Partner',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/reports.xml',
        'views/agreement.xml',
        'views/agreement_clause.xml',
        'views/agreement_section.xml',
        'views/agreement_serviceprofile.xml',
        'views/agreement_stages.xml',
        'views/agreement_type.xml',
        'views/agreement_subtype.xml',
        'views/res_partner.xml',
        #'security/security.xml',
        #'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
