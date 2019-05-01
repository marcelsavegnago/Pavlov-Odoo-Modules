# Copyright (C) 2018 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

{
    'name': 'Pavlov Media - Field Service',
    'summary': 'Pavlov Media Configuration and Data for Field Service',
    'version': '12.0.1.0.0',
    'license': 'Other proprietary',
    'author': 'Pavlov Media',
    'maintainer': 'Pavlov Media',
    'website': 'https://www.pavlovmedia.com',
    'depends': ['base',
                'fieldservice',
                'partner_sensitivity',
                'contacts',
                ],
    'data': [
        'views/fsm_location.xml',
        'views/fsm_order.xml',
        'views/menu.xml',
    ],
    'application': True,
    'development_status': 'Beta',
    'maintainers': ['patrickrwilson'],
}
