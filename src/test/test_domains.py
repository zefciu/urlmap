try:
    import unittest2 as unittest
except ImportError:
    import unittest

from util import make_app
import os
import sys
from paste.deploy import loadapp
from webtest import TestApp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE)

class Test(unittest.TestCase):
    """Testing multiple domain configuration"""

    def setUp(self):
        self.mapper = loadapp('config:test_domains.ini', relative_to=HERE)

    def test_map(self):
        app = TestApp(self.mapper)
        res = app.get('/', extra_environ={'HTTP_HOST': 'example.com'})
        res.mustcontain('ec80root')
        res = app.get(
            '/foo', extra_environ={'HTTP_HOST': 'example.com'}
        )
        res.mustcontain('ec80foo')
        res = app.get(
            '/', extra_environ={'HTTP_HOST': 'example.net'}
        )
        res.mustcontain('en80root')
        res = app.get(
            '/', extra_environ={'HTTP_HOST': 'example.com:8080'}
        )
        res.mustcontain('ec8080root')
