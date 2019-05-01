{
    'name': "External Systems (R&D)",
    'summary': """Fields and Form changes for R&D Integration into Pebbles
                   and Houston.""",
    'author': "Pavlov Media",
    'website': "https://www.pavlovmedia.com",
    'category': 'Extra Tool',
    'version': '12.0.1.0.0',
    'depends': ['base',
                'mail',
                'product',
                'fieldservice',
                'stock'],
    'data': [
        'views/fsm_location.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'security/security.xml',
        'views/res_config_view.xml',
    ],
    'application': True,
}
