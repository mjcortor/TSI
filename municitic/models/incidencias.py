# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Incidencias(models.Model):
    _name = 'municitic.incidencias'
    _description = 'Municitic Incidencias'
    name = fields.Char(string="Nombre", required=True, help="nombre de la incidencia")
    description = fields.Text()
    ubicacion = fields.Text()
    start = fields.Datetime('Fecha y Hora',required=True, autodate = True)
    end = fields.Datetime('Fecha y Hora',required=True, autodate = True)   
    activityType = fields.Selection([('urbanistico','Urbanístico'),#tipo incidencia renombrar
                                    ('emergencia','Emergencia'),
                                    ('trafico','Tráfico'),],
                                    'Tipo de incidencia')
    valoraciones_ids = fields.Many2one("municitic.valoraciones",string="Valoraciones confirmadas")
    trabajadores_ids = fields.Many2many("municitic.trabajadores",string="Trabajadores confirmados")
    usuarios_ids = fields.Many2one("municitic.usuarios",string="Usuarios confirmados")