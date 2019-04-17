# -*- coding: utf-8 -*-
{
    'name': "Pavlov Media Customizations",

    'summary': """
        Pavlov Media Customizations""",

    'description': """
        This module contains customizations only for Pavlov Media.
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tool',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                'fieldservice',
                'helpdesk',
                'helpdesk_scope',            
                ],

    # always loaded
    'data': [
        'views/res_partner.xml',
        'views/fsm_location.xml',
        'views/fsm_resident_type.xml',
        'views/fsm_building_type.xml',
        'views/fsm_order.xml',
        'views/helpdesk_ticket.xml',
        'security/ir.model.access.csv',
        'data/building_type_data.xml',
        'data/resident_type_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
