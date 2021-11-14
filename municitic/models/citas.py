# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Citas(models.Model):
    _name = 'municitic.citas'
    _description = 'Municitic Citas'
    titulo = fields.Char(string="Titulo", required=True, help="nombre de la cita")
    description = fields.Text()
    asistentes = fields.Integer("Numero de asistentes")
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',required=True, autodate = True)
    tipoCita = fields.Selection([('sugerencia','Sugerencia'),
                                    ('incidencia','Incidencia'),
                                    ('pregunta','Preguntas'),],
                                    'Tipo de cita')
    usuarios_ids = fields.Many2many("municitic.usuarios",string="Usuarios confirmados")
    trabajadores_ids = fields.Many2one("municitic.trabajadores",string="Trabajadores confirmados")
