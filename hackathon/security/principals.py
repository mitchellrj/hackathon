# $Id$
# encoding: utf-8
"""hackathon.security.principals"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]


ADMIN = 'admin'


def user(id_=None, user=None):
    if user is not None:
        id_ = user.id
    if id_ is None:
        raise ValueError
    return 'user#{}'.format(id_)
