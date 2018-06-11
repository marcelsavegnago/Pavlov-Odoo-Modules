# -*- coding: utf-8 -*-
{
    'name': "Pavlov Project Milestones",

    'summary': """
        Pavlov Media Project Milestones""",

    'description': """
        This module adds Milestones to the Project model for Pavlov Media
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'project'],

    # always loaded
    'data': [
        'views/project_milestone.xml',
        'views/project.xml',
        'views/project_task.xml',
        #'security/security.xml',
        #'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
}
