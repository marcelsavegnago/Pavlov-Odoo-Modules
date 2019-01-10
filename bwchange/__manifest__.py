# -*- coding: utf-8 -*-
{
    'name': "Pavlov Bandwidth Change",

    'summary': """
        Bandwidth Changes for Pavlov Media""",

    'description': """
        Bandwidth Changes module for Pavlov Media
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bandwidth Changes',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'report/bwchange_reports.xml',
        'views/bwchange.xml',
        'views/bwchange_owner.xml',
        'views/bwchange_speed.xml',
        'views/bwchange_stage.xml',
        'views/bwchange_qtreetype.xml',
        'views/res_partner.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/bwchange_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
