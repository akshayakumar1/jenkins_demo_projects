# -*- coding: utf-8 -*-
# from odoo import http


# class TestControllers(http.Controller):
#     @http.route('/test_controllers/test_controllers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_controllers/test_controllers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_controllers.listing', {
#             'root': '/test_controllers/test_controllers',
#             'objects': http.request.env['test_controllers.test_controllers'].search([]),
#         })

#     @http.route('/test_controllers/test_controllers/objects/<model("test_controllers.test_controllers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_controllers.object', {
#             'object': obj
#         })
