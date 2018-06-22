# -*- coding: utf-8 -*-
{
    'name': "Partner Agreements Entitlements",

    'summary': """
        Partner Agreements Entitlements""",

    'description': """
        This module adds Entitlements to the Partner Agreement Module.

        Requires:
        - Maintenance (Used for linking equipment)
        - Helpdesk (Helpdesk SLA's need to be enabled)
        - Sales
        - Partner Agreements
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Agreements',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'partner_agreement', 'helpdesk', 'sale_management', 'maintenance'],

    # always loaded
    'data': [
        'views/agreement.xml',
        'views/agreement_entitlement.xml',
        'views/res_partner.xml',
        'views/helpdesk_sla.xml',
        'views/helpdesk_ticket.xml',
        'views/equipment.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
