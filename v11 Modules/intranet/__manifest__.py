# -*- coding: utf-8 -*-
{
    'name': "Intranet SharePoint Server",

    'summary': """
        Intranet SharePoint Server""",

    'description': """
        This module provides a link to a Intranet SharePoint server within Odoo.
    """,

    'author': "Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/server_intranet.xml',
        'views/res_config_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}