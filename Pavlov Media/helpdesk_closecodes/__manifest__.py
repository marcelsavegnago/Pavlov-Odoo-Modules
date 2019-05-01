{
    'name': "Helpdesk - Close Codes",

    'summary': """
        Helpdesk - Close Codes""",

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        'views/helpdesk.xml',
        'views/helpdesk_close_cause.xml',
        'views/helpdesk_close_action.xml',
        'views/helpdesk_ticket_type.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
