# $Id$
# encoding: utf-8
"""hackathon.models.submission"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import hashlib

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import orm
from sqlalchemy import types

from hackathon.models.base import Base
from hackathon.models.entry import Entry
from hackathon.storage.interfaces import IFileStorage


def file_identifier(data):
    return hashlib.new('SHA1', data).hexdigest()


class Submission(Base):

    @property
    def __acl__(self):
        return self.entry.__acl__

    entry_id = Column(types.Integer, ForeignKey(Entry.id))
    text = Column(types.UnicodeText, default='')
    file_identifier = Column(types.String, nullable=True)
    file_content_type = Column(types.String, nullable=True)
    file_name = Column(types.String, nullable=True)
    storage_name = Column(types.String, nullable=True)

    entry = orm.relationship(Entry, backref='submissions', uselist=False)

    def get_file(self, request):
        settings = request.registry.settings
        storage = request.registry.getAdapter(settings,
                                              IFileStorage,
                                              name=self.storage_name)
        return storage.get_file(self.file_identifier)

    def set_file(self, request, data):
        settings = request.registry.settings
        storage_name = settings.get('hackathon.storage')
        storage = request.registry.getAdapter(settings,
                                              IFileStorage,
                                              name=storage_name)
        self.storage_name = storage_name
        identifier = storage.add_file(None, data)
        self.file_identifier = identifier
