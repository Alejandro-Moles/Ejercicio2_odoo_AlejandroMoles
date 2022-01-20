# -*- coding: utf-8 -*-
# from odoo import http


# class Ejercicio2Odoo(http.Controller):
#     @http.route('/ejercicio2__odoo/ejercicio2__odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejercicio2__odoo/ejercicio2__odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejercicio2__odoo.listing', {
#             'root': '/ejercicio2__odoo/ejercicio2__odoo',
#             'objects': http.request.env['ejercicio2__odoo.ejercicio2__odoo'].search([]),
#         })

#     @http.route('/ejercicio2__odoo/ejercicio2__odoo/objects/<model("ejercicio2__odoo.ejercicio2__odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejercicio2__odoo.object', {
#             'object': obj
#         })
