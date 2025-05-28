# file: project_scrum/__manifest__.py
{
    'name': "Project Scrum Management",
    'version': '1.0',
    'depends': ['base', 'project', 'planning', 'hr_timesheet'],
    'author': "YourName",
    'category': 'Project Management',
    'summary': "Modulo Scrum avanzato per gestire progetti, sprint e user stories in Odoo",
    'description': """
Gestione avanzata di progetti Scrum:
- Backlog separato per ogni progetto
- Sprint con date configurabili e stato
- User Stories con story points e Task collegati
- Velocity degli sprint e burndown chart giornaliero
- Kanban personalizzati, Gantt e Dashboard Scrum
- Ruoli Product Owner, Scrum Master, Developer
- Retrospective e Sprint Review
- Integrazione con Timesheet e Planning
    """,
    'data': [
        'security/scrum_security.xml',
        'security/ir.model.access.csv',
        'data/scrum_demo_data.xml',
        'data/ir_cron.xml',
        'views/scrum_menu.xml',
        'views/scrum_sprint_views.xml',
        'views/scrum_story_views.xml',
        'views/scrum_retrospective_views.xml',
        'views/scrum_review_views.xml',
        'views/scrum_dashboard_views.xml',
        'views/scrum_task_views.xml',
    ],
    'demo': [
        'demo/scrum_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
