# -*- coding: utf-8 -*-
{
    'name': "Project Enhancements - Timesheet Timer",

    'summary': """
        Project Enhancements - Timesheet Timer""",

    'description': """
        This module adds a Start/Stop Timer to the Project Tasks model.
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project_timesheet_forecast'],

    # always loaded
    'data': [
        'views/project_task_view.xml',
        'wizards/timesheet_entry_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
