# file: project_scrum/models/scrum_sprint.py
from odoo import models, fields, api
from datetime import date

class ScrumSprint(models.Model):
    _name = 'scrum.sprint'
    _description = 'Sprint Scrum'
    _rec_name = 'name'
    _order = 'start_date desc'

    name = fields.Char(string="Nome Sprint", required=True)
    project_id = fields.Many2one('project.project', string="Progetto", required=True)
    start_date = fields.Date(string="Data Inizio", required=True)
    end_date = fields.Date(string="Data Fine", required=True)
    state = fields.Selection([
        ('planned', "Pianificato"),
        ('in_progress', "In Corso"),
        ('done', "Chiuso")
    ], string="Stato", default='planned')
    story_ids = fields.One2many('scrum.user.story', 'sprint_id', string="User Stories")
    velocity = fields.Integer(string="Velocity", compute='_compute_velocity', store=True)
    burndown_line_ids = fields.One2many('scrum.burndown.line', 'sprint_id', string="Burndown")

    @api.depends('story_ids', 'story_ids.story_points', 'story_ids.state')
    def _compute_velocity(self):
        for sprint in self:
            # Calcola la somma degli story point di tutte le user story completate (state='done')
            total = 0
            for story in sprint.story_ids:
                if story.state == 'done':
                    total += story.story_points
            sprint.velocity = total


    def compute_burndown_lines(self):
        today = fields.Date.context_today(self)
        for sprint in self.search([('state', '!=', 'done')]):
            if sprint.start_date and sprint.end_date:
                # Calcola story point rimanenti
                remaining = 0
                for story in sprint.story_ids:
                    if story.state != 'done':
                        remaining += story.story_points
                # Crea record burndown per oggi se non esiste
                line = self.env['scrum.burndown.line'].search([
                    ('sprint_id','=', sprint.id), ('date','=', today)], limit=1)
                if not line:
                    self.env['scrum.burndown.line'].create({
                        'sprint_id': sprint.id,
                        'date': today,
                        'remaining_points': remaining,
                    })
                else:
                    line.remaining_points = remaining


# file: project_scrum/models/scrum_sprint.py (continuazione)

class ScrumBurndownLine(models.Model):
    _name = 'scrum.burndown.line'
    _description = 'Linea del Burndown Chart (story point rimanenti)'

    sprint_id = fields.Many2one('scrum.sprint', string="Sprint", required=True, ondelete='cascade')
    date = fields.Date(string="Data", required=True)
    remaining_points = fields.Integer(string="Story Points Rimanenti")
