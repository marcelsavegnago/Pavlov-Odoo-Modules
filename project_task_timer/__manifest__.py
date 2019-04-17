# -*- coding: utf-8 -*-
{
    'name': "Project Task Timer",

    'summary': """
        Project Task Timer""",

    'description': """
        This module adds a Start/Stop Timer to the Project Tasks model.
    """,

    'author': "Patrick Wilson, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/project",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['project',
                'hr_timesheet',
                'timesheet_grid'],

    # always loaded
    'data': [
        'views/project_task_view.xml',
        'views/timer.xml',
        'wizards/task_timesheet_entry_view.xml',
        'wizards/timer_warning.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
