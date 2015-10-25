import logging.config

from pyramid.config import Configurator
import asyncio
import sys
import json


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # support logging in python3
    logging.config.fileConfig(
        settings['logging.config'],
        disable_existing_loggers=False
    )

    config = Configurator(settings=settings)

    config.include('pyramid_raven')

    return config.make_wsgi_app()
