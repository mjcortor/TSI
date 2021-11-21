# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tipotrabajador(models.Model):
    _name = 'municitic.tipotrabajador'
    _description = 'Municitic Trabajador'
    tipoTrabajador = fields.Selection([('politico','Politico'),
                                    ('personal_laboral','Personal laboral'),
                                    ('personal_eventual','Personal eventual'),
                                    ('personal_funcionario','Personal funcionario'),],
                                    'Tipo de trabajador')
    
    trabajadores_ids = fields.One2many("municitic.trabajadores","tipotrabajador_ids","Trabajador confirmado")
    comunicados_ids = fields.One2many("municitic.comunicados","tipotrabajador_ids","Comunicado confirmado")