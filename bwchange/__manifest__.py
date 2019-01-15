# -*- coding: utf-8 -*-
{
    'name': "Bandwidth Changes",

    'summary': """
        Bandwidth Changes""",

    'description': """
        Bandwidth Changes module used for Pavlov Media to track when circuit changes happen, the information associated with those changes and to assist with the Bandwidth Change process.
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bandwidth Changes',
    'version': '12.0.1.0.0',

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
