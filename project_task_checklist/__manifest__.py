{
    'name': "Project Task Checklists",

    'summary': """
        Project Task Checklists""",

    'author': "Patrick Wilson, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/project",

    'category': 'Project Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'views/project_task.xml',
        'views/project_task_checklist.xml',
        'security/ir.model.access.csv',
    ],

    'application': False,
    'development_status': 'Beta',
    'maintainers': ['patrickrwilson'],
}
