# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Incidencias(models.Model):
    _name = 'municitic.incidencias'
    _description = 'Municitic Incidencias'
    name = fields.Char(string="Nombre", required=True, help="nombre de la incidencia")
    description = fields.Text()
    ubicacion = fields.Text()
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',required=True, autodate = True)   
    activityType = fields.Selection([('urbanistico','Urbanístico'),
                                    ('emergencia','Emergencia'),
                                    ('trafico','Tráfico'),],
                                    'Tipo de incidencia')
    nTrabajadores = fields.Integer(compute='_nTrabajadores',string='Trabajadores total',store=True)
    valoraciones_ids = fields.Many2one("municitic.valoraciones",string="Valoraciones confirmadas")
    trabajadores_ids = fields.Many2many("municitic.trabajadores",string="Trabajadores confirmados")
    usuarios_ids = fields.Many2one("municitic.usuarios",string="Usuarios confirmados")
    
    
    @api.depends('trabajadores_ids')
    def _nTrabajadores(self): 
        for record in self:                            
            record.nTrabajadores = len(record.trabajadores_ids)