{
    'name': "Helpdesk - KB Documents",

    'summary': """
        Adds related KB Documents to Ticket Tags""",

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    'category': 'Helpdesk',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk', 'documents'],

    # always loaded
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_tag.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
