# -*- coding: utf-8 -*-
{
    'name': "Project Enhancements",

    'summary': """
        Project Types, Status, Department and Progress""",

    'description': """
        This module adds Project Types, Status, Department and Progress to the Project model.
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
    'depends': ['base', 'project', 'timesheet_grid', 'hr', 'project_forecast'],

    # always loaded
    'data': [
        'report/sprint_capacity_report.xml',
        'views/project_status.xml',
        'views/project_type.xml',
        'views/project.xml',
        'views/project_task.xml',
        'views/project_task_type.xml',
        'views/res_config_settings_views.xml',
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
    'application':True,
}
