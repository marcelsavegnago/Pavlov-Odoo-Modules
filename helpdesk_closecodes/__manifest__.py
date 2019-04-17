# -*- coding: utf-8 -*-
{
    'name': "Helpdesk - Close Codes",

    'summary': """
        Helpdesk - Close Codes""",

    'description': """
        This module adds close codes to the Helpdesk model.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_close_cause.xml',
        'views/helpdesk_close_action.xml',
        'views/helpdesk_ticket_type.xml',
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
