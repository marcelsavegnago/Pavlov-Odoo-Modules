# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.
{
    'name': 'Power BI Report Server',
    'summary': 'Power BI Report Server',
    'author': 'Pavlov Media',
    'website': 'https://www.pavlovmedia.com',
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'license': 'Other proprietary',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/server_powerbi.xml',
        'views/res_config_view.xml',
    ],
    'application': True,
}
