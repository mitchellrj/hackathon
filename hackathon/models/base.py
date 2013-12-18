# $Id$
# encoding: utf-8
"""hackathon.models.base"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import datetime

from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
import pytz
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.ext.declarative import declarative_base

from hackathon.security.principals import ADMIN


class AbstractBase:

    __acl__ = (Allow, ADMIN, ALL_PERMISSIONS)

    id = Column(types.Integer, primary_key=True)
    created = Column(types.DateTime(timezone=True),
                     default=datetime.datetime.now(tz=pytz.UTC))
    modified = Column(types.DateTime(timezone=True),
                      onupdate=datetime.datetime.now(tz=pytz.UTC))


Base = declarative_base(cls=AbstractBase)
