# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

{
    'name': "Helpdesk - KB Documents",
    'summary': "Adds related KB Documents to Ticket Tags.",
    'author': "Pavlov Media",
    'website': "https://www.pavlovmedia.com",
    'category': 'Extra Tool',
    'version': '12.0.1.0.0',
    'depends': ['base',
                'helpdesk',
                'documents'],
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_tag.xml',
    ],
}
