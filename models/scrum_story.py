# file: project_scrum/models/scrum_story.py
from odoo import models, fields, api, exceptions

class ScrumUserStory(models.Model):
    _name = 'scrum.user.story'
    _description = 'User Story Scrum'
    _rec_name = 'name'

    name = fields.Char(string="Titolo", required=True)
    description = fields.Text(string="Descrizione")
    story_points = fields.Integer(string="Story Points", required=True)
    project_id = fields.Many2one('project.project', string="Progetto", required=True)
    sprint_id = fields.Many2one('scrum.sprint', string="Sprint")
    task_ids = fields.One2many('project.task', 'story_id', string="Task", readonly=True)
    state = fields.Selection([
        ('draft', "Nuova"),
        ('in_progress', "In Lavorazione"),
        ('done', "Completata")
    ], string="Stato", default='draft')
    date_start = fields.Date(string="Data Inizio")
    date_end = fields.Date(string="Data Fine")

    @api.constrains('story_points')
    def _check_story_points(self):
        for record in self:
            if record.story_points < 0:
                raise exceptions.ValidationError("Gli Story Points devono essere >= 0")
