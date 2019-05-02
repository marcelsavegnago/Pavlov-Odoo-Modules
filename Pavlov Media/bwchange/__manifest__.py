# Copyright (c) 2018 - TODAY, Pavlov Media <https://www.pavlovmedia.com>
# License Proprietary. Do not copy, share nor distribute.

{
    'name': 'Bandwidth Changes',
    'summary': 'Bandwidth Changes',
    'author': 'Patrick Wilson: Pavlov Media',
    'website': 'https://www.pavlovmedia.com',
    'category': 'Bandwidth Changes',
    'version': '12.0.1.0.0',
    'license': 'Other proprietary',
    'depends': ['mail',
                'fieldservice'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'data/bwchange_owner.xml',
        'data/bwchange_speed.xml',
        'data/bwchange_qtreetype.xml',
        'data/bwchange_stage.xml',
        'report/bwchange_reports.xml',
        'views/bwchange.xml',
        'views/bwchange_owner.xml',
        'views/bwchange_speed.xml',
        'views/bwchange_stage.xml',
        'views/bwchange_qtreetype.xml',
        'views/res_partner.xml',
        'views/fsm_location.xml',
    ],
    'application': True,
}
