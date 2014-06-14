# -*- coding: utf-8 -*-
"""
    flask_markdown
    ~~~~~~~~~~~~~~

    A flask extension to add markdown support.

    :copyright: (c) 2013 by Daniel Chatfield
    :copyright: (c) 2014 by Veniamin Gvozdikov
"""

from jinja2_markdown import MarkdownExtension

class markdown(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MARKDOWN_EXTENSIONS', ['extra'])
        app.config.setdefault('MARKDOWN_EXTCONFIGS', {})
        app.jinja_env.add_extension(MarkdownExtension)
