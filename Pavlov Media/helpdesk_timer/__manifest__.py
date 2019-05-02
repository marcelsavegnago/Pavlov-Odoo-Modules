# Copyright (C) 2018 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

{
    'name': "Helpdesk Timer",
    'summary': "Adds timer functionality to Helpdesk Tickets",
    'author': "Pavlov Media",
    'website': "https://www.pavlovmedia.com",
    'category': 'Extra Tool',
    'version': '12.0.1.0.0',
    'depends': ['helpdesk',
                'helpdesk_timesheet',
                'project_task_timer'],
    'data': [
        'views/helpdesk_ticket_view.xml',
        'views/timer.xml',
        'wizards/timer_warning.xml',
    ],
}
