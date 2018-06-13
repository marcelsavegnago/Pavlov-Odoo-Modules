# -*- coding: utf-8 -*-
{
    'name': "Sales Territories",

    'summary': """
        Sales Territories""",

    'description': """
        This module adds Sales Territories to the Partner model.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Partner',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'views/sales_territories.xml',
        'views/res_partner.xml',
        'views/res_users.xml'
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
