# $Id$
# encoding: utf-8
"""hackathon.routes"""
__author__ = 'Richard Mitchell <richard.mitchell@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]


def configure_routes(config):

    config.add_route('home', '/')
    config.add_route('login', '/login')
