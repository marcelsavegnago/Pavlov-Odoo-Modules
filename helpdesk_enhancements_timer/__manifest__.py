# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Enhancements - Timesheet Timer",

    'summary': """
        Helpdesk Enhancements - Timesheet Timer""",

    'description': """
        This module adds a Start/Stop Timer to the Helpdesk model.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk', 'helpdesk_timesheet'],

    # always loaded
    'data': [
        'views/helpdesk_ticket_view.xml',
        'wizards/ticket_timesheet_entry_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
