# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Comunicados(models.Model):
    _name = 'municitic.comunicados'
    _description = 'Municitic Comunicados'
    name = fields.Char(string="Titulo", required=True, help="nombre del comunicado")
    descripcion = fields.Text()
    start = fields.Datetime('Comienza',required=True, autodate = True)   
    tipoComunicado = fields.Selection([('noticia','Noticia'),
                                    ('actividad','Actividad'),],
                                    'Tipo de comunicado')
    
    usuarios_ids = fields.Many2many("municitic.usuarios",string="Usuario confirmado")
    tipotrabajador_ids = fields.Many2one("municitic.tipotrabajador",string="Tipo Trabajador confirmado")
    valoraciones_ids = fields.Many2one("municitic.valoraciones",string="Valoraciones confirmadas")
    