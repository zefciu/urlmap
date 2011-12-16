import os
import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paste.deploy import loadapp
from urlmap.test.util import make_app

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE)

class Test(unittest.TestCase):
    """Throw error when path specified as 'domain'"""

    def _broken(self):
        return loadapp('config:test_port_only.ini', relative_to=HERE)

    def test_port_only(self):
        self.assertRaises(ValueError, self._broken)
