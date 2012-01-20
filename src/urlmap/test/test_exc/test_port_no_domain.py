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
    """Throw error when port specified but no domain"""

    def _broken(self):
        return loadapp('config:test_port_no_domain.ini', relative_to=HERE)

    def test_port_twice(self):
        self.assertRaises(ValueError, self._broken)
