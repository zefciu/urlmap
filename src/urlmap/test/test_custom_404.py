try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
import sys

from webtest import TestApp
from paste.deploy import loadapp

from urlmap.test.util import make_app

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE)


def app404(global_conf):
    def app(environ, start_response):
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response('404 Not Found', headers)
        response_text = """<html><head><title>Not found</title></head><body>
<p>This is not the page you're looking for</p></body></html>"""
        return [(response_text % environ).encode('utf-8')]
    return app
        

class Test(unittest.TestCase):
    """Testing behaviors with custom 404 application"""

    def setUp(self):
        self.mapper = loadapp('config:test_custom_404.ini', relative_to=HERE)

    def test_404(self):
        app = TestApp(self.mapper)
        res = app.get('/', status=404)
        res.mustcontain('not the page you')

