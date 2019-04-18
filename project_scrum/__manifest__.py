{
    'name': "Project Scrum",

    'summary': """
        Project Scrum""",

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
        'report/sprint_capacity_report.xml',
        'views/project.xml',
        'views/project_forecast.xml',
        'views/project_scrum_sprint.xml',
        'views/project_scrum_category.xml',
        'views/project_scrum_issuetype.xml',
        'views/project_scrum_label.xml',
        'views/project_scrum_point.xml',
        'views/project_scrum_release.xml',
        'views/project_scrum_source.xml',
        'views/project_scrum_epic.xml',
        'views/project_task.xml',
        'views/project_scrum_team.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
