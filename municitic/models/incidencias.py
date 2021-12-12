# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Incidencias(models.Model):
    _name = 'municitic.incidencias'
    _description = 'Municitic Incidencias'
    name = fields.Char(string="Nombre", required=True, help="nombre de la incidencia")
    description = fields.Text()
    ubicacion = fields.Text()
    start = fields.Datetime('Comienza',required=True, autodate = True)
    end = fields.Datetime('Finaliza',autodate = True)   
    activityType = fields.Selection([('urbanistico','Urbanístico'),
                                    ('emergencia','Emergencia'),
                                    ('trafico','Tráfico'),],
                                    'Tipo de incidencia')
    estado = fields.Selection([('resuelta','Resuelta'),
                                     ('cancelada','Cancelada'),
                                     ('encurso','En Curso'),],
                                     'Estado', default='encurso')
    nTrabajadores = fields.Integer(compute='_nTrabajadores',string='Trabajadores total',store=True)
    valoraciones_ids = fields.Many2one("municitic.valoraciones",string="Valoraciones confirmadas")
    trabajadores_ids = fields.Many2many("municitic.trabajadores",string="Trabajadores confirmados")
    usuarios_ids = fields.Many2one("municitic.usuarios",string="Usuarios confirmados")
    
    
    @api.depends('trabajadores_ids')
    def _nTrabajadores(self): 
        for record in self:                            
            record.nTrabajadores = len(record.trabajadores_ids)
            
    def btn_submit_to_resuelta(self):
          self.write({'estado':'resuelta'})

    def btn_submit_to_cancelada(self):
          self.write({'estado':'cancelada'})
          
    def btn_submit_to_encurso(self):
          self.write({'estado':'encurso'})
          
    @api.onchange('trabajadores_ids')
    def onchange_trabajadores(self):
        if self.name != False and self.estado == 'cancelada':   # el false de name sirve para que no se ejecute el onchange al pulsar el boton "Create"
            raise models.ValidationError('La incidencia ya está cancelada')
        elif self.name != False and self.estado == 'resuelta':
            raise models.ValidationError('La incidencia ya está resuelta')
        
    @api.onchange('usuarios_ids')
    def onchange_usuarios(self):
        if self.name != False and self.estado == 'cancelada':  # el false de name sirve para que no se ejecute el onchange al pulsar el boton "Create"
            raise models.ValidationError('La incidencia ya está cancelada')
        elif self.name != False and self.estado == 'resuelta':
            raise models.ValidationError('La incidencia ya está resuelta')
        
    @api.constrains('end','estado')
    def _check_end(self):
        if self.estado == 'resuelta' and self.end == False:
            raise models.ValidationError('La incidencia está resuelta, se le debe agregar una fecha de finalización')