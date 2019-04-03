# -*- coding: utf-8 -*-
{
    'name': "Project - Pavlov Media",

    'summary': """
        Pavlov Media Project changes""",

    'description': """
        This module adds Project items specific to Pavlov Media
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'project'],

    # always loaded
    'data': [
        'views/project.xml',
        'views/project_task.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':False,
}
