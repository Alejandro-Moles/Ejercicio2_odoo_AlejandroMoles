# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejercicio2__odoo(models.Model):
#     _name = 'ejercicio2__odoo.ejercicio2__odoo'
#     _description = 'ejercicio2__odoo.ejercicio2__odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




from odoo import models, fields, api

class coche(models.Model):
	_name = 'ejercicio2__odoo.coche'
	_description = 'model coche'

	Codigo = fields.Char('Codigo',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	color = fields.Char(string='Color',required=True)

class cliente(models.Model):
	_name = 'ejercicio2__odoo.cliente'
	_description = 'model cliente'

	Dni = fields.Char('Dni',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True)


class pedido(models.Model):
	_name = 'ejercicio2__odoo.pedido'
	_description = 'model pedido'

	Codigo = fields.Char('Codigo',required=True)
	coche = fields.Char(string='Coche',required=True)
	