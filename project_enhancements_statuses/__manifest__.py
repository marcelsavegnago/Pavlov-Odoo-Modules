# -*- coding: utf-8 -*-
{
    'name': "Project Enhancements - Statuses",

    'summary': """
        Project Status""",

    'description': """
        This module adds Project Statuses to the Project model.
        Dependencies: Projects, Timesheets, Employees, Forecasts
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project_enhancements'],

    # always loaded
    'data': [
        'views/project_status.xml',
        'views/project.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':False,
}
