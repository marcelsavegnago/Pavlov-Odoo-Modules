# -*- coding: utf-8 -*-
{
    'name': "Project Auto Forecasts",

    'summary': """
        Project Auto Forecasts""",

    'description': """
        This module adds Auto Forecasting to the Project model.
    """,

    'author': "Patrick Wilson, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/project",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['project',
                'timesheet_grid',
                'hr',
                'project_forecast'],

    # always loaded
    'data': [

        'views/project.xml',
        'views/project_task.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
