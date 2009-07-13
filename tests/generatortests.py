#!/usr/bin/env python

"""Unit tests for slingshot generator"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','lib'))

import generator

class SlingshotTestCase(unittest.TestCase):
  def testDefault(self):
    assert True


if __name__ == "__main__":
  unittest.main()

