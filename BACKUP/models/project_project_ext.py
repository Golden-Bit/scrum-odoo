# project_scrum/models/project_project_ext.py
from odoo import api, fields, models

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type = fields.Selection([
        ('standard', 'Standard'),
        ('scrum',    'Scrum'),
    ], string='Tipo di Progetto', default='standard')

    def write(self, vals):
        res = super().write(vals)
        # only when you switch to Scrum
        if 'project_type' in vals:
            for project in self.filtered(lambda p: p.project_type == 'scrum'):
                project._ensure_scrum_stages()
        return res

    def _ensure_scrum_stages(self):
        """Create / reorder Scrum-specific stages on project.task.type."""
        Stage = self.env['project.task.type']
        SCRUM_STAGES = [
            'Backlog',
            'Stories Todo',
            'Task Todo',
            'Subtask Todo',
            'Stories In Progress',
            'Task In Progress',
            'Subtask In Progress',
            'Stories Done',
            'Task Done',
            'Subtask Done',
        ]
        # find all stages already linked to this project
        existing = Stage.search([('project_ids', 'in', self.id)])
        existing_names = existing.mapped('name')
        for idx, name in enumerate(SCRUM_STAGES, start=1):
            stage = existing.filtered(lambda s: s.name == name)
            if stage:
                # just update sequence
                stage.sequence = idx
                # ensure still linked
                if self not in stage.project_ids:
                    stage.write({'project_ids': [(4, self.id)]})
            else:
                # create and link
                Stage.create({
                    'name':        name,
                    'sequence':    idx,
                    'project_ids': [(4, self.id)],
                })
