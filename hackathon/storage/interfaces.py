# $Id$
# encoding: utf-8
"""hackathon.storage.interfaces"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from zope.interface import Interface


class IFileStorage(Interface):

    def __init__(self, settings):
        """Initialize the storage.
           @param settings:
           @type settings: dict
        """

    def add_file(self, identifier, data):
        """Adds a file to storage.

           @param identifier: A unique identifier for the data. If
                              None, a new identifier will be generated.
           @type identifier: bytes
           @param data: The file data to be stored.
           @type data: file or bytes
           @raise ValueError: If this data already exists in storage.
           @return: The identifier of the file.
           @rtype: str
        """

    __setitem__ = add_file

    def get_file(self, identifier):
        """Retrieves a file from storage.
           @param identifier: The identifier returned when this file
                              was added to storage.
           @type identifier: str
           @raise KeyError: If this identifier cannot be found in
                            storage.
           @return: A file-like object containing the file data.
           @rtype: file
        """

    __getitem__ = get_file

    def del_file(self, identifier):
        """Deletes a file from storage.
           @param identifier: The identifier returned when this file
                              was added to storage.
           @type identifier: str
           @raise KeyError: If this identifier cannot be found in
                            storage.
        """

    __delitem__ = del_file

    def has_file(self, identifier):
        """Determines if an identifier exists in storage
           @param identifier: The identifier returned when this file
                              was added to storage.
           @type identifier: str
           @return: True if the identifier exists within this storage.
           @rtype: bool
        """

    __contains__ = has_file
