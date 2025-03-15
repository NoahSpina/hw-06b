# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 should be a Scalene triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles', '3,3,4 should be an Isosceles triangle')

    def testNotATriangle(self):
        # The sum of two sides (1 + 2) is not greater than the third (3)
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a valid triangle')

    def testZeroSide(self):
        # A side length of 0 should be considered invalid
        self.assertEqual(classifyTriangle(0, 2, 3), 'InvalidInput', '0,2,3 should be invalid input')

    def testNegativeSide(self):
        # Negative side lengths should be flagged as invalid
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', '-1,2,3 should be invalid input')

    def testLargeScaleneTriangle(self):
        # Testing with larger numbers to ensure scalability
        self.assertEqual(classifyTriangle(10, 15, 17), 'Scalene', '10,15,17 should be a Scalene triangle')

    def testFloatingPointRightTriangle(self):
        # Floating point numbers should work correctly
        self.assertEqual(classifyTriangle(3.0, 4.0, 5.0), 'Right', '3.0,4.0,5.0 is a Right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

