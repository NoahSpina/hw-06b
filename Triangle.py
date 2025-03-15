# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

import math

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # Check if inputs are numeric (int or float)
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return 'InvalidInput'

    # Check range: each side must be between 0 and 200 (exclusive of 0)
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check for positive side lengths
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Check triangle inequality:
    # The sum of any two sides must be greater than the third side.
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Now we know we have a valid triangle.
    # Check for Equilateral triangle
    if a == b == c:
        return 'Equilateral'

    # Check for a Right triangle using the Pythagorean theorem on all permutations.
    if math.isclose(a ** 2 + b ** 2, c ** 2) or \
            math.isclose(a ** 2 + c ** 2, b ** 2) or \
            math.isclose(b ** 2 + c ** 2, a ** 2):
        return 'Right'

    # Check for Scalene triangle (all sides different)
    if a != b and b != c and a != c:
        return 'Scalene'

    # Otherwise, it's an Isosceles triangle (exactly two sides equal)
    return 'Isosceles'
