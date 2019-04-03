# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Timer",

    'summary': """
        Helpdesk Timer""",

    'description': """
        This module adds a Start/Stop Timer to the Helpdesk model.
    """,

    'author': "Patrick Wilson, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/project",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk',
                'helpdesk_timesheet',
                'project_task_timer'],

    # always loaded
    'data': [
        'views/helpdesk_ticket_view.xml',
        'views/timer.xml',
        'wizards/timer_warning.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
