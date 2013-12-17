# $Id$
# encoding: utf-8
"""hackathon.models.entry"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Allow
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import orm
from sqlalchemy import types

from hackathon.models.base import Base
from hackathon.models.hackathon import Hackathon
from hackathon.models.task import Task
from hackathon.models.user import User
from hackathon.security.principals import user


entry_tasks = Table(
    'entry_tasks',
    Base.metadata,
    Column('entry_id', types.Integer, ForeignKey('Entry.id')),
    Column('task_id', types.Integer, ForeignKey(Task.id)),
    )


class Entry(Base):

    @property
    def __acl__(self):
        return Base.__acl__ + [
            (Allow, user(self.user_id), ALL_PERMISSIONS),
            ]

    hackathon_id = Column(types.Integer, ForeignKey(Hackathon.id))
    user_id = Column(types.Integer, ForeignKey(User.id))

    hackathon = orm.relationship(Hackathon, uselist=False)
    user = orm.relationship(User, uselist=False)

    # Configured by Submission
    submissions = []

    _tasks = orm.relationship(Task, secondary=entry_tasks)

    @property
    def tasks(self):
        """After creation, we shouldn't be able to change tasks."""

        return self._tasks
