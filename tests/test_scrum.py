# file: project_scrum/tests/test_scrum.py
from odoo.tests import TransactionCase


class TestScrumModule(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Project = self.env['project.project']
        self.Sprint = self.env['scrum.sprint']
        self.Story = self.env['scrum.user.story']

        # Creo un progetto di test
        self.proj = self.Project.create({'name': 'Proj Test'})
        # Creo uno sprint
        self.sprint = self.Sprint.create({
            'name': 'Sprint Test',
            'project_id': self.proj.id,
            'start_date': '2025-01-01',
            'end_date': '2025-01-15',
            'state': 'in_progress'
        })
        # Creo alcune user story
        self.story1 = self.Story.create({
            'name': 'US1', 'story_points': 3,
            'project_id': self.proj.id, 'sprint_id': self.sprint.id,
            'state': 'done'
        })
        self.story2 = self.Story.create({
            'name': 'US2', 'story_points': 5,
            'project_id': self.proj.id, 'sprint_id': self.sprint.id,
            'state': 'in_progress'
        })

    def test_velocity(self):
        # A sprint in corso con 1 story done (3 punti) e 1 in_progress (5 punti)
        self.assertEqual(self.sprint.velocity, 3, "La velocity dovrebbe essere la somma degli story point completati")

    def test_story_to_sprint_assignment(self):
        # Controlla che la story sia associata allo sprint corretto
        self.assertEqual(self.story1.sprint_id.id, self.sprint.id)
