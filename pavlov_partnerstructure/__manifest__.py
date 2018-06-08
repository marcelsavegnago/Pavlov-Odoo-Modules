# -*- coding: utf-8 -*-
{
    'name': "Pavlov Partner Structure",

    'summary': """
        Pavlov Media Partner Buildings, Floors, Units""",

    'description': """
        This module adds Buildings, Floors and Units to the partner models for Pavlov Media
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Partner',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/partner_buildings.xml',
        'views/partner_floors.xml',
        'views/partner_units.xml',
        'views/res_partner.xml',
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
