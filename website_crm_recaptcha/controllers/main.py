# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.addons.web import http
from openerp.addons.web.http import request
import openerp.addons.website_crm.controllers.main as main


class ContactUs(main.contactus):

    @http.route(['/crm/contactus'], type='http', auth="public",
                website=True, multilang=True)
    def contactus(self, *args, **kw):
        response = kw.pop('g-recaptcha-response', None)
        if not kw or not response:
            if 'kwargs' not in kw:
                kw['kwargs'] = kw.items()
        elif request.website.is_captcha_valid(response):
            return super(ContactUs, self).contactus(*args, **kw)
        else:
            if 'kwargs' not in kw:
                kw['kwargs'] = kw.items()
            kw['error'] = set(['recaptcha_response_field'])
        return request.website.render("website.contactus", kw)
