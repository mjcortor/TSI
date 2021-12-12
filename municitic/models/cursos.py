# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cursos(models.Model):
    _name = 'municitic.cursos'
    _description = 'Municitic Cursos'
    name = fields.Char(string="Titulo", required=True, help="nombre de la cita")
    description = fields.Text()
    asistentes = fields.Integer("Numero de asistentes")
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',required=True, autodate = True)
    tipoCurso = fields.Selection([('informatica','Informatica'),
                                    ('riesgosLaborales','Riesgos Laborales'),
                                    ('idiomas','Idiomas'),],
                                    'Tipo de curso')
    trabajadores_ids = fields.Many2many("municitic.trabajadores",string="Trabajadores confirmados")
