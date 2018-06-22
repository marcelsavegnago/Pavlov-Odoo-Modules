# -*- coding: utf-8 -*-
{
    'name': "Partner Agreements Service Profiles",

    'summary': """
        Partner Agreements Service Profiles""",

    'description': """
        This module adds Service Profiles to the Partner Agreement Module.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Agreements',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'partner_agreement'],

    # always loaded
    'data': [
        'views/agreement.xml',
        'views/agreement_serviceprofile.xml',
        'views/res_partner.xml',
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
