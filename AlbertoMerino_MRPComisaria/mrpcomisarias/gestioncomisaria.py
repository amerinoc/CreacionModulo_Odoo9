#-*- coding: utf-8 -*-
from openerp import models, fields, api

class Policias(models.Model):
	_name = 'comisaria.policias'
	placa = fields.Char('Placa', required = True, size = 8)
	nombre = fields.Char('Nombre', required = True, size = 150)
	edad = fields.Integer('Edad', required = True)
	localidad = fields.Char('Localidad', required = True)
	patrulla = fields.Many2one('comisaria.patrullas', 'Patrulla')
	
class Patrullas(models.Model):
	_name = 'comisaria.patrullas'
	idpatrulla = fields.Integer('Patrulla', required = True)
	nombrepatrulla = fields.Char('Nombre de la patrulla', required = True)
	zonapatrulla = fields.Char('Zona', required = True)
	policiasenpatrulla = fields.One2many('comisaria.policias','patrulla','policia')
	