# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Valoraciones(models.Model):
    _name = 'municitic.valoraciones'
    _description = 'Municitic Valoraciones'
    valoracion = fields.Integer()
    comentario = fields.Text()
    
    citas_ids = fields.One2many("municitic.citas","valoraciones_ids","Cita confirmada")
    incidencias_ids = fields.One2many("municitic.incidencias","valoraciones_ids","Incidencia confirmada")
    comunicados_ids = fields.One2many("municitic.comunicados","valoraciones_ids","Comunicado confirmado")