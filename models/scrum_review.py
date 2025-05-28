# file: project_scrum/models/scrum_review.py
from odoo import models, fields

class ScrumSprintReview(models.Model):
    _name = 'scrum.sprint.review'
    _description = 'Sprint Review'

    name = fields.Char(string="Nome Review", required=True)
    sprint_id = fields.Many2one('scrum.sprint', string="Sprint", required=True)
    summary = fields.Text(string="Riepilogo della Review")
    date = fields.Date(string="Data Review", default=fields.Date.context_today)
