import sys
from unittest import TestCase

from proctor.tests import settings


class PrivateViewsTest(TestCase):
    def test_import(self):
        # FIXME: Add real tests! Import module to ensure that test suite tests top-level code:
        sys.modules['settings'] = settings
        from proctor.views import private  # noqa
