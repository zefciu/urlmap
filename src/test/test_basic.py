try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
import sys
from urlmap import URLMap
from webtest import TestApp
from paste.deploy import loadapp


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE)


def make_app(global_conf, app_name):
    text = '%s script_name="%%(SCRIPT_NAME)s" path_info="%%(PATH_INFO)s"'
    response_text = text % app_name
    def app(environ, start_response):
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response('200 OK', headers)
        return [(response_text % environ).encode('utf-8')]
    return app


class Test(unittest.TestCase):
    """Various tests for urlmap"""

    def setUp(self):
        self.mapper = loadapp('config:test_basic.ini', relative_to=HERE)

    def test_map(self):
        app = TestApp(self.mapper)
        res = app.get('/')
        res.mustcontain('root')
        res.mustcontain('script_name=""')
        res.mustcontain('path_info="/"')
        res = app.get('/blah')
        res.mustcontain('root')
        res.mustcontain('script_name=""')
        res.mustcontain('path_info="/blah"')
        res = app.get('/foo/and/more')
        res.mustcontain('script_name="/foo"')
        res.mustcontain('path_info="/and/more"')
        res.mustcontain('foo-only')
        res = app.get('/foo/bar/baz')
        res.mustcontain('foo:bar')
        res.mustcontain('script_name="/foo/bar"')
        res.mustcontain('path_info="/baz"')
        res = app.get('/fffzzz')
        res.mustcontain('root')
        res.mustcontain('path_info="/fffzzz"')
        res = app.get('/f/z/y')
        res.mustcontain('script_name="/f"')
        res.mustcontain('path_info="/z/y"')
        res.mustcontain('f-only')
    
    def test_404(self):
        self.mapper = URLMap()
        app = TestApp(self.mapper, extra_environ={'HTTP_ACCEPT': 'text/html'})
        res = app.get("/-->%0D<script>alert('xss')</script>", status=404)
        assert '--><script' not in res.unicode_body
        res = app.get("/--%01><script>", status=404)
        assert '--\x01><script>' not in res.unicode_body
