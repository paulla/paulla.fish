import os

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.threadlocal import get_current_registry

here = os.path.dirname(os.path.abspath(__file__))


def main(global_config, **settings):
    # configuration settings

    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')
    settings['db'] = os.path.join(here, 'fish.db')
    get_current_registry().settings = settings

    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    config.include('pyramid_chameleon')
    # routes setup

    config.add_route('listing', '/')
    config.add_route('new', '/new')
    config.add_route('close', '/close/{id}')
    config.add_route('dl', '/dl/{id}/{fname}')
    config.add_route('detail', '/detail/{id}/{fname}')
    # static view setup
    config.add_static_view('static', os.path.join(here, 'static'))
    # scan for @view_config and @subscriber decorators
    config.scan()
    return config.make_wsgi_app()
