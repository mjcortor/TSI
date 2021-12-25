# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cursos(models.Model):
    _name = 'municitic.cursos'
    _description = 'Municitic Cursos'
    name = fields.Char(string="Titulo", required=True, help="nombre de la cita")
    description = fields.Text()
    capacidad = fields.Integer("Numero de asistentes")
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',required=True, autodate = True)
    tipoCurso = fields.Selection([('informatica','Informatica'),
                                    ('riesgosLaborales','Riesgos Laborales'),
                                    ('idiomas','Idiomas'),],
                                    'Tipo de curso')
    trabajadores_ids = fields.Many2many("municitic.trabajadores",string="Trabajadores confirmados")

    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 25:
            raise models.ValidationError('El título del curso no debe sobrepasar 25 carácteres')
        
    @api.onchange('capacidad','tipoCurso')
    def onchange_cursos(self):
          resultado = {}
          if self.capacidad >= 10 and self.tipoCurso == 'informatica':
               resultado = {
                    'value': {'capacidad':10},
                    'warning': {
                         'title':'Valores incorrectos',
                         'message':'Las cursos de informática no deben superar las 10 personas'
                    }
               }
               return resultado
