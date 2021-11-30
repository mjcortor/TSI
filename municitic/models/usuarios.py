# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Usuarios(models.Model):
    _name = 'municitic.usuarios'
    _description = 'Municitic Usuarios'
    name = fields.Char(string="Nombre", required=True, help="nombre completo")
    dni = fields.Char(string="DNI", required=True, help="dni")
    usuario = fields.Char(string="Usuario", required=True, help="usuario")
    direccion = fields.Text()
    photo=fields.Binary('Photo')
    
    citas_ids = fields.Many2many("municitic.citas",string="Cita confirmada")
    incidencias_ids = fields.One2many("municitic.incidencias","usuarios_ids","Incidencia confirmada")
    comunicados_ids = fields.Many2many("municitic.comunicados",string="Comunicado confirmado")
