# Copyright (C) 2018 Open Source Integrators
# License Proprietary. Do not copy, share nor distribute.
{
    'name': "Project Task Timer",
    'summary': "Adds a timer to project tasks.",
    'author': "Pavlov Media",
    'website': "https://www.pavlovmedia.com",
    'category': 'Extra Tool',
    'version': '12.0.1.0.0',
    'depends': ['project',
                'hr_timesheet',
                'timesheet_grid'],
    'data': [
        'views/project_task_view.xml',
        'views/timer.xml',
        'wizards/task_timesheet_entry_view.xml',
        'wizards/timer_warning.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
