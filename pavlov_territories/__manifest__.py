# -*- coding: utf-8 -*-
{
    'name': "Pavlov Territories",

    'summary': """
        Pavlov Media Territories""",

    'description': """
        This module adds Sales and Service Territories to the Partner model for Pavlov Media
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
        'views/partner_salesterritories.xml',
        'views/partner_serviceterritories.xml',
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
