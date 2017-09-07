#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from scrapy.exceptions import NotConfigured
from scrapy_stackdriver import StackDriverLogger

class TestScrapyStackdriver(unittest.TestCase):
    """Ensure we can create the StackDriverLogger object."""

    def test_creates_object(self):
        """Creating the object with a project name raises no error"""
        leaded = StackDriverLogger("test-case")

    def test_requires_project_name(self):
        """The project name is required."""

        self.assertRaises(NotConfigured, StackDriverLogger)

if __name__ == "__main__":
    unittest.main()
