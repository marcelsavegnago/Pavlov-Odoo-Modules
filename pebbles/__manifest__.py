# -*- coding: utf-8 -*-
{
    'name': "Pebbles Customizations",

    'summary': """
        Pebbles Customizations""",

    'description': """
        This module adds Pavlov Media's customizations for Pebbles integration.
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tool',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/res_partner.xml',
#        'security/security.xml',
#        'security/ir.model.access.csv',
#        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
