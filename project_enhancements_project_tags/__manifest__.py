# -*- coding: utf-8 -*-
{
    'name': "Project Enhancements - Project Tags",

    'summary': """
        Project Tags""",

    'description': """
        This module adds Project Tags used on Tasks to the Project model.
        Dependencies: Projects, Timesheets, Employees, Forecasts
    """,

    'author': "Patrick Wilson: Pavlov Media",
    'website': "https://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project_enhancements'],

    # always loaded
    'data': [
        'views/project.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':False,
}
