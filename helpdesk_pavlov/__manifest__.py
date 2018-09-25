# -*- coding: utf-8 -*-
{
    'name': "Helpdesk - Pavlov Customizations",

    'summary': """
        Pavlov Media Helpdesk Customizations""",

    'description': """
        This module adds Pavlov Media specific customizations to the Helpdesk model.
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
        #'views/helpdesk_origin.xml',
        'views/helpdesk.xml',
        'views/helpdesk_topic.xml',
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
