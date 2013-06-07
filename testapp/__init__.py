import datetime
import time 

from pyramid.config import Configurator
from pyramid.renderers import JSON


json_renderer = JSON()


def datetime_adapter(obj, request):
    return obj.isoformat()


json_renderer.add_adapter(datetime.datetime, datetime_adapter)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('json', json_renderer)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
