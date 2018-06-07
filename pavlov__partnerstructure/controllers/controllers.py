# -*- coding: utf-8 -*-
from odoo import http

# class PavlovBwchange(http.Controller):
#     @http.route('/pavlov__bwchange/pavlov__bwchange/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pavlov__bwchange/pavlov__bwchange/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pavlov__bwchange.listing', {
#             'root': '/pavlov__bwchange/pavlov__bwchange',
#             'objects': http.request.env['pavlov__bwchange.pavlov__bwchange'].search([]),
#         })

#     @http.route('/pavlov__bwchange/pavlov__bwchange/objects/<model("pavlov__bwchange.pavlov__bwchange"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pavlov__bwchange.object', {
#             'object': obj
#         })