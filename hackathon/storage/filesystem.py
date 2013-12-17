# $Id$
# encoding: utf-8
"""hackathon.storage.filesystem"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

import configparser

from zope.interface import implementer

from hackathon.storage.interfaces import IFileStorage


@implementer(IFileStorage)
class FilesystemStorage:

    def __init__(self, settings):
        