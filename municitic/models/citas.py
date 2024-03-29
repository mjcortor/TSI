# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Citas(models.Model):
    _name = 'municitic.citas'
    _description = 'Municitic Citas'
    name = fields.Char(string="Titulo", required=True, help="nombre de la cita")
    description = fields.Text()
    asistentes = fields.Integer(compute='_asistentesTotal',string='Asistentes total',store=True)
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',required=True, autodate = True)
    tipoCita = fields.Selection([('sugerencia','Sugerencia'),
                                    ('incidencia','Incidencia'),
                                    ('pregunta','Preguntas'),],
                                    'Tipo de cita')
    usuarios_ids = fields.Many2many("municitic.usuarios",string="Usuarios confirmados")
    trabajadores_ids = fields.Many2one("municitic.trabajadores",string="Trabajadores confirmados")
    valoraciones_ids = fields.One2many("municitic.valoraciones","citas_ids","Valoraciones confirmadas")
    
    def btn_borrarUsuariosCita(self):
          self.write({'usuarios_ids':[(5,)]})
          
    @api.depends('usuarios_ids')
    def _asistentesTotal(self): 
          for record in self:
               record.asistentes = len(record.usuarios_ids)
          
    @api.constrains('asistentes')
    def _check_asistentes(self):
          if self.asistentes > 3:
                raise models.ValidationError('Debido a las restricciones del COVID-19 las citas no pueden superar los 3 asistentes.')
    