# -*- coding: utf-8 -*-
{
    'name': "Helpdesk - KB Documents",

    'summary': """
        Adds related KB Documents to Ticket Tags""",

    'description': """
        This module adds related Knowledgebase Documents to the Helpdesk model by linking them to the Ticket Tags.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk', 'documents'],

    # always loaded
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_tag.xml',
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
