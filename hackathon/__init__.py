from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from sqlalchemy import engine_from_config

from hackathon.models import initialize_sql


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_beaker')
    config.include('pyramid_tm')
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)

    config.scan('hackathon.views')
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    return config.make_wsgi_app()
