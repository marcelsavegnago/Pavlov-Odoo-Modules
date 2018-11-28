# -*- coding: utf-8 -*-
{
    'name': "Project Scrum",

    'summary': """
        Project Scrum""",

    'description': """
        This module adds Scrum & Sprints to the Project model.
        Depends: Projects, Timesheets, Employees
    """,

    'author': "Pavlov Media",
    'website': "http://www.pavlovmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'timesheet_grid', 'hr'],

    # always loaded
    'data': [
        'report/sprint_capacity_report.xml',
        'views/project.xml',
        'views/project_scrum_sprint.xml',
        'views/project_scrum_category.xml',
        'views/project_scrum_issuetype.xml',
        'views/project_scrum_label.xml',
        'views/project_scrum_point.xml',
        'views/project_scrum_release.xml',
        'views/project_scrum_source.xml',
        'views/project_task.xml',
        'views/project_scrum_team.xml',
        'views/project_task_type.xml',
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
