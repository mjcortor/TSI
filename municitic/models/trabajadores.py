# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Trabajadores(models.Model):
    _name = 'municitic.trabajadores'
    _description = 'Municitic Trabajadores'
    nombre = fields.Char(string="Nombre", required=True, help="nombre completo")
    dni = fields.Char(string="DNI", required=True, help="dni")
    usuario = fields.Char(string="Usuario", required=True, help="usuario")
    direccion = fields.Text()
    photo=fields.Binary('Photo')
    
    citas_ids = fields.One2many("municitic.citas","trabajadores_ids","Cita confirmada")
    incidencias_ids = fields.Many2many("municitic.incidencias",string="Incidencias confirmados")
    tipotrabajador_ids = fields.Many2one("municitic.tipotrabajador",string="Tipo Trabajador confirmado")
    cursos_ids = fields.Many2many("municitic.cursos",string="Cursos confirmados")

