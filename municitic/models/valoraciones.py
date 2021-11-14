# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Valoraciones(models.Model):
    _name = 'municitic.valoraciones'
    _description = 'Municitic Valoraciones'
    valoracion = fields.Integer()
    comentario = fields.Text()
