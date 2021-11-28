# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Valoraciones(models.Model):
    _name = 'municitic.valoraciones'
    _description = 'Municitic Valoraciones'
    name = fields.Char(string="Nombre", required=True, help="nombre de la valoracion")
    valoracion = fields.Integer("Valoracion")
    comentario = fields.Text()
    
    citas_ids = fields.Many2one("municitic.citas",string="Citas confirmadas")
    incidencias_ids = fields.One2many("municitic.incidencias","valoraciones_ids","Incidencia confirmada")
    comunicados_ids = fields.One2many("municitic.comunicados","valoraciones_ids","Comunicado confirmado")
