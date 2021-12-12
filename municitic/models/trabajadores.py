# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Trabajadores(models.Model):
    _name = 'municitic.trabajadores'
    _description = 'Municitic Trabajadores'
    name = fields.Char(string="Nombre", required=True, help="nombre completo")
    dni = fields.Char(string="DNI", required=True, help="dni")
    usuario = fields.Char(string="Usuario", required=True, help="usuario")
    direccion = fields.Text()
    photo=fields.Binary('Photo')
    nIncidencias = fields.Integer(compute='_nIncidencias',string='Incidencias total',store=True)
    
    citas_ids = fields.One2many("municitic.citas","trabajadores_ids","Cita confirmada")
    incidencias_ids = fields.Many2many("municitic.incidencias",string="Incidencias confirmados")
    tipotrabajador_ids = fields.Many2one("municitic.tipotrabajador",string="Tipo Trabajador confirmado")
    cursos_ids = fields.Many2many("municitic.cursos",string="Cursos confirmados")

    @api.depends('incidencias_ids')
    def _nIncidencias(self): 
        for record in self:                            
            record.nIncidencias = len(record.incidencias_ids)