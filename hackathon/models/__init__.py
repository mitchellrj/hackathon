# $Id$
# encoding: utf-8
"""hackathon.models"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from hackathon.models.base import Base
from hackathon.models.session import DBSession


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)  # @UndefinedVariable
