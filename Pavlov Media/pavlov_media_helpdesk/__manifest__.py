# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

{
    'name': 'Pavlov Media - Helpdesk',
    'summary': 'Pavlov Media Configuration and Data for Helpdesk',
    'version': '12.0.1.0.0',
    'license': 'Other proprietary',
    'author': 'Pavlov Media',
    'maintainer': 'Pavlov Media',
    'website': 'https://www.pavlovmedia.com',
    'depends': ['base',
                'mail',
                'helpdesk',
                'helpdesk_scope',
                'helpdesk_phone',
                'helpdesk_resolution',
                'helpdesk_ticket_parent',
                'helpdesk_ticket_type_default_priority',
                ],
    'data': [
        'views/helpdesk_ticket.xml',
        'views/menu.xml',
    ],
    'development_status': 'Beta',
    'maintainers': ['patrickrwilson'],
}
