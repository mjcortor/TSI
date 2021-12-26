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
    
    _sql_constraints = [('usuarios_dni_unique','UNIQUE (dni)','El dni debe ser único')]
    
    _sql_constraints = [('usuarios_usuario_unique','UNIQUE (usuario)','El usuario debe ser único')]

    @api.constrains('dni')
    def _check_dni(self):
        if len(self.dni) != 9:
            raise models.ValidationError('El dni debe tener una longitud de 9')
        elif len(self.dni) == 9:
            letra = self.dni[8]
            subs = self.dni[0:7]
            if(letra.isdigit()):
                raise models.ValidationError('El dni debe tener una letra al final')
            elif(subs.isdigit() == False):
                raise models.ValidationError('El dni no debe contener números en los 8 primeros carácteres')
            
    