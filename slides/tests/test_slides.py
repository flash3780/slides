#!/usr/bin/env python

import unittest
import slides

class SlideTests(unittest.TestCase):
    def test_validate_path(self):
        self.assertEqual(validate_path('/usr/bin'),'/usr/bin')