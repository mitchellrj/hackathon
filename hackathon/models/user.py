# $Id$
# encoding: utf-8
"""hackathon.models.user"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import pbkdf2
from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.ext.declarative import synonym_for

from hackathon.models.base import Base
from hackathon.security.principals import user


class User(Base):

    @property
    def __acl__(self):
        return Base.__acl__ + [
            (Allow, user(self.id), ALL_PERMISSIONS),
            ]

    name = Column(types.Unicode)
    email = Column(types.Unicode)
    _password = Column(type.String, name='password')

    @synonym_for('_password')
    @property
    def password(self):
        return ''

    @password.setter
    def password(self, value):
        # salt=None defaults to a random salt
        # iterations=None defaults to 400
        self._password = pbkdf2.crypt(value,
                                      salt=None,
                                      iterations=None)

    def authenticate(self, password):
        # Passing the existing password as the salt gets the salt &
        # iteration count used to hash that.
        hash_ = pbkdf2.crypt(password,
                             salt=self._password,
                             iterations=None)
        return hash_ == self._password
