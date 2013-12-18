# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.0'

requires = [
    'deform',
    'pbkdf2',
    'pyramid',
    'pyramid_beaker',
    'pytz',
    'SQLAlchemy',
    'pyramid_tm',
    # For SQLAlchemy tie-in with transactions
    'zope.sqlalchemy',
    ]

test_requires = [
    ]

setup(
    name='hackathon',
    version=version,
    description="",
    keywords='',
    author='Richard Mitchell',
    author_email='richard.mitchell@isotoma.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require=dict(
        test=test_requires
        ),
    entry_points="""
    [paste.app_factory]
    main = hackathon:main
    """,
    )
