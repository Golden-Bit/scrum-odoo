# project_scrum/models/project_project_ext.py
from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'
    project_type = fields.Selection([
        ('standard', 'Standard'),
        ('scrum', 'Scrum'),
        ('agile', 'Agile')
    ], string='Tipo di Progetto', default='standard')
