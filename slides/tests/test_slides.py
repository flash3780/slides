#!/usr/bin/env python

import unittest

from slides import slides

class SlideTests(unittest.TestCase):
    def test_validate_path(self):
        self.assertEqual(slides.validate_path('/usr/bin'),'/usr/bin')
