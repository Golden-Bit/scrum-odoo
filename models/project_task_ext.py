# project_scrum/models/project_task_ext.py
from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'
    story_points = fields.Integer(string='Story Points')
    sprint_id = fields.Many2one('project.sprint', string='Sprint')
    # Campo related per project_type del progetto padre, per usare nelle viste
    project_type = fields.Selection(related='project_id.project_type', readonly=True, string='Project Type')
