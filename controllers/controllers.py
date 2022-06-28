# -*- coding: utf-8 -*-
# from odoo import http


# class Saleperson(http.Controller):
#     @http.route('/saleperson_mandatory_empty/saleperson_mandatory_empty', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saleperson_mandatory_empty/saleperson_mandatory_empty/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('saleperson_mandatory_empty.listing', {
#             'root': '/saleperson_mandatory_empty/saleperson_mandatory_empty',
#             'objects': http.request.env['saleperson_mandatory_empty.saleperson_mandatory_empty'].search([]),
#         })

#     @http.route('/saleperson_mandatory_empty/saleperson_mandatory_empty/objects/<model("saleperson_mandatory_empty.saleperson_mandatory_empty"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saleperson_mandatory_empty.object', {
#             'object': obj
#         })
