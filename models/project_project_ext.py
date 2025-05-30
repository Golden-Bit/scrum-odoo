from odoo import api, fields, models, _

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type = fields.Selection([
        ('standard', 'Standard'),
        ('scrum', 'Scrum'),
    ], string='Tipo di Progetto', default='standard')

    @api.model_create_multi
    def create(self, vals_list):
        projects = super().create(vals_list)
        # Dopo creazione, genera fasi se è Scrum
        for project in projects.filtered(lambda p: p.project_type == 'scrum'):
            project._ensure_scrum_stages()
        return projects

    def write(self, vals):
        res = super().write(vals)
        # Se cambio tipo in “scrum”, genera fasi
        if 'project_type' in vals:
            for project in self.filtered(lambda p: p.project_type == 'scrum'):
                project._ensure_scrum_stages()
        return res

    def _ensure_scrum_stages(self):
        """Assicura che il progetto abbia le 7 fasi Scrum nell’ordine corretto."""
        Stage = self.env['project.task.type']
        sequence_map = {
            'Backlog': 1,
            'Task Todo': 2,
            'Subtask Todo': 3,
            'Task In Progress': 4,
            'Subtask In Progress': 5,
            'Task Done': 6,
            'Subtask Done': 7,
        }
        # Estrae nomi già esistenti nel progetto
        existing = self.stage_ids.mapped('name')
        # Crea quelle mancanti e assegna la sequence
        for name, seq in sequence_map.items():
            stage = self.stage_ids.filtered(lambda s: s.name == name)
            if stage:
                # Riassegna comunque la sequence per garantire l’ordine
                stage.sequence = seq
            else:
                Stage.create({
                    'name': name,
                    'sequence': seq,
                    'project_ids': [(4, self.id)],
                })
