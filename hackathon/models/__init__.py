# $Id$
# encoding: utf-8
"""hackathon.models"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import transaction

from hackathon.models.base import Base
from hackathon.models.entry import Entry
from hackathon.models.hackathon import Hackathon
from hackathon.models.submission import Submission
from hackathon.models.task import Task
from hackathon.models.user import User
from hackathon.models.session import DBSession


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)  # @UndefinedVariable

    session = DBSession()
    if not session.query(User).filter(User.email=='richard.mitchell@isotoma.com').first():
        user = User(email='richard.mitchell@isotoma.com',
                    name='Richard Mitchell')
        user.password = 'foo'
        session.add(user)
        transaction.commit()
