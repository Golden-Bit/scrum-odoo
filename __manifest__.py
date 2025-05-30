{
    'name': "Project Scrum Extension",
    'version': '18.0.1.0.0',
    'category': 'Project',
    'summary': 'Aggiunge story points e sprint ai task (visibili solo per progetti Scrum)',
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_task_kanban_views.xml',
        'project_task_search_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
