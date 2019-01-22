# -*- coding: utf-8 -*-
{
    'name': "Example - FSM Location Builder",

    'summary': """
        Example - FSM Location Builder""",

    'description': """
        Example - FSM Location Builder
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
        'views/fsm_location_hierarchy_wizard.xml',
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
