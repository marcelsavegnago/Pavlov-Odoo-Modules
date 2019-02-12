# -*- coding: utf-8 -*-
{
    'name': "Project Enhancements - Auto Forecasts",

    'summary': """
        Project Auto Forecasts""",

    'description': """
        This module adds Auto Forecasting to the Project model.
        Dependencies: Projects, Project Enhancements, Timesheets, Employees, Forecasts
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
                'project',
                'timesheet_grid',
                'hr',
                'project_forecast',
                'project_enhancements'],

    # always loaded
    'data': [

        'views/project.xml',
        'views/project_task.xml',
#        'security/security.xml',
#        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':False,
}
