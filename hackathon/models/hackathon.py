# $Id$
# encoding: utf-8
"""hackathon.models.hackathon"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from sqlalchemy import Column
from sqlalchemy import types

from hackathon.models.base import Base


class Hackathon(Base):

    name = Column(types.Unicode)
    start = Column(types.DateTime)
    end = Column(types.DateTime)
    brief = Column(types.UnicodeText)
    task_count = Column(types.Integer, nullable=True)
    random_task_assignment = Column(types.Boolean, default=False)

    # Configured by Task
    available_tasks = []
