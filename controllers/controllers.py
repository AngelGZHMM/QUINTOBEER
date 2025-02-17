# -*- coding: utf-8 -*-
# from odoo import http


# class Quintobeer(http.Controller):
#     @http.route('/quintobeer/quintobeer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quintobeer/quintobeer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quintobeer.listing', {
#             'root': '/quintobeer/quintobeer',
#             'objects': http.request.env['quintobeer.quintobeer'].search([]),
#         })

#     @http.route('/quintobeer/quintobeer/objects/<model("quintobeer.quintobeer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quintobeer.object', {
#             'object': obj
#         })
