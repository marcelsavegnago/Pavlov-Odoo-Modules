# -*- coding: utf-8 -*-
{
    'name': "Example - FSM Location",

    'summary': """
        Example - FSM Location""",

    'description': """
        Example - FSM Location
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/fsm_location.xml',
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
