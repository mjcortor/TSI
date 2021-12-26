# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Comunicados(models.Model):
    _name = 'municitic.comunicados'
    _description = 'Municitic Comunicados'
    name = fields.Char(string="Titulo", required=True, help="nombre del comunicado")
    descripcion = fields.Text()
    emision = fields.Datetime('Emision',required=True, autodate = True)   
    tipoComunicado = fields.Selection([('noticia','Noticia'),
                                    ('actividad','Actividad'),],
                                    'Tipo de comunicado')
    
    usuarios_ids = fields.Many2many("municitic.usuarios",string="Usuario confirmado")
    tipotrabajador_ids = fields.Many2one("municitic.tipotrabajador",string="Tipo Trabajador confirmado")
    valoraciones_ids = fields.Many2one("municitic.valoraciones",string="Valoraciones confirmadas")
    
    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 50:
            raise models.ValidationError('El título del comunicado no debe sobrepasar 50 carácteres')
        
    def btn_generate_report(self):
          return self.env.ref('municitic.report_comunicados').report_action(self)