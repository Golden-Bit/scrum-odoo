# project_scrum/models/project_sprint.py
from odoo import models, fields

class ProjectSprint(models.Model):
    _name = 'project.sprint'
    _description = 'Project Sprint'
    name = fields.Char(string='Nome Sprint', required=True)
    date_start = fields.Date(string='Data Inizio')
    date_end = fields.Date(string='Data Fine')
    project_id = fields.Many2one('project.project', string='Progetto', required=True)
    #???
    sequence = fields.Integer(string='Sequenza', default=10)
