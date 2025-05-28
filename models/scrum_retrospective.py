# file: project_scrum/models/scrum_retrospective.py
from odoo import models, fields

class ScrumSprintRetrospective(models.Model):
    _name = 'scrum.sprint.retrospective'
    _description = 'Sprint Retrospective'

    name = fields.Char(string="Titolo Retrospective", required=True)
    sprint_id = fields.Many2one('scrum.sprint', string="Sprint", required=True)
    notes = fields.Text(string="Note della Retrospective")
    date = fields.Date(string="Data Retrospective", default=fields.Date.context_today)
