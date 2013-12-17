from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from hackathon.models import initialize_sql


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_tm')

    config.scan('hackathon.views')
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    return config.make_wsgi_app()
