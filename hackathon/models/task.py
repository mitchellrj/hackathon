# $Id$
# encoding: utf-8
"""hackathon.models.task"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import orm
from sqlalchemy import types


from hackathon.models.base import Base
from hackathon.models.hackathon import Hackathon


class Task(Base):

    __tablename__ = 'tasks'

    hackathon_id = Column(types.Integer, ForeignKey(Hackathon.id))
    name = Column(types.Unicode)

    hackathon = orm.relationship(Hackathon,
                                 backref='available_tasks')
