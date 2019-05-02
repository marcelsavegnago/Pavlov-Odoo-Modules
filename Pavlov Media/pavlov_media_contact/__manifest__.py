# Copyright (C) 2019 Pavlov Media
# License Proprietary. Do not copy, share nor distribute.

{
    'name': 'Pavlov Media - Contact/Partner',
    'summary': 'Pavlov Media Configuration and Data for Contact/Partner',
    'version': '12.0.1.0.0',
    'license': 'Other proprietary',

    'author': 'Pavlov Media',
    'maintainer': 'Pavlov Media',
    'website': 'https://www.pavlovmedia.com',
    'depends': ['base',
                'partner_sensitivity',
                'fieldservice',
                'helpdesk',
                'pavlov_media_fieldservice',
                ],
    'data': [
        'views/res_partner.xml',
    ],
    'development_status': 'Beta',
    'maintainers': ['patrickrwilson'],
}
