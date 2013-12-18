# $Id$
# encoding: utf-8
"""hackathon.storage.filesystem"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import hashlib
import io
import os
import tempfile

from zope.interface import implementer

from hackathon.storage.interfaces import IFileStorage


@implementer(IFileStorage)
class FilesystemStorage:

    def __init__(self, settings):
        self.directory = os.path.abspath(settings.get('fss.directory', ''))

    def valid_identifier(self, identifier, raise_=False):
        result = True
        if not len(identifier):
            result = False
        elif os.path.sep in identifier:
            result = False
        else:
            absolute_path = os.path.abspath(
                    os.path.join(self.directory, identifier)
                )
            result = absolute_path.startswith(self.directory)
        return result

    def validate_identifier(self, identifier):
        if not self.valid_identifier(identifier):
            raise ValueError('Invalid identifier, {!r}.'.format(identifier))
        return True

    def _get_path(self, identifier):
        return os.path.abspath(
                os.path.join(self.directory, identifier)
            )

    def add_file(self, identifier=None, data=None):
        if identifier:
            self.validate_identifier(identifier)

        new_identifier = identifier is None
        hash_ = hashlib.new('SHA1')
        filepath = ''

        if not new_identifier:
            filepath = self._get_path(identifier)
            if self.has_file(identifier):
                raise ValueError(
                        'File already exists with identifier, {!r}'.format(
                            identifier
                            )
                    )

        fh, temp_path = tempfile.mkstemp()
        if hasattr(data, 'read'):
            last_read_bytes = -1
            while last_read_bytes != 0:
                buf = data.read(1024)
                last_read_bytes = len(buf)
                if last_read_bytes:
                    if new_identifier:
                        hash_.update(buf)
                    fh.write(buf)
        elif isinstance(data, bytes):
            if new_identifier:
                hash_.update(data)
            fh.write(data)

        fh.close()
        if new_identifier:
            identifier = hash_.hexdigest()
            filepath = self._get_path(identifier)

        os.rename(temp_path, filepath)

        return identifier

    __setitem__ = add_file

    def has_file(self, identifier):
        self.validate_identifier(identifier)
        filepath = self._get_path(identifier)
        return os.path.exists(filepath)

    __contains__ = has_file

    def get_file(self, identifier):
        self.validate_identifier(identifier)
        if not self.has_file(identifier):
            raise KeyError('No file exists with identifier, {!r}.'.format(
                            identifier
                        ))
        filepath = self._get_path(identifier)
        return io.BufferedReader(open(filepath, 'rb'))

    __getitem__ = get_file

    def del_file(self, identifier):
        self.validate_identifier(identifier)
        if not self.has_file(identifier):
            raise KeyError('No file exists with identifier, {!r}.'.format(
                            identifier
                        ))
        filepath = self._get_path(identifier)
        os.unlink(filepath)

    __delitem__ = del_file
