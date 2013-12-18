# $Id$
# encoding: utf-8
"""hackathon.views.login"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from pyramid.httpexceptions import HTTPCreated
from pyramid.security import remember
from pyramid.view import view_config

from hackathon.models.session import DBSession
from hackathon.models.user import User


class LoginView:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='login', request_method='GET',
                 renderer='templates/login_form.pt')
    def show_login_form(self):
        return {}

    @view_config(route_name='login', request_method='POST',
                 renderer='templates/login_failed.pt')
    def process_login(self, success_response_cls=HTTPCreated):
        email = self.request.params.get('email')
        password = self.request.params.get('password')

        session = DBSession()
        user = session.query(User).filter(User.email == email).first()
        headers = {}
        success = False
        if user:
            success = user.authenticate(password)
        if success:
            headers = remember(self.request, user.id)

            home_page = self.request.route_url('home')
            came_from = self.request.session.get('came_from',
                                                 home_page)
            headers.append(('Location', came_from))

            return success_response_cls(headers=headers)

        self.request.response.status_code = 403
        return {}
