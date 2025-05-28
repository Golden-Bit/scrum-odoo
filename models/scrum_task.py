# file: project_scrum/models/scrum_task.py
from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    story_id = fields.Many2one('scrum.user.story', string="User Story")
