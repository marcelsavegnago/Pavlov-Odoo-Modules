# -*- coding: utf-8 -*-
{
    'name': "Pavlov Pebbles Integration Customizations",

    'summary': """
        Pavlov Media Pebbles Integration Customizations""",

    'description': """
        This module adds Pavlov Media specific pebbles integration customizations to Odoo.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_ticket_type.xml',
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
