#Stevens Institute of Technology - Fall 2022
# SSW 567 - Software Testing, Quality Assurance and Maintenance
# Nathalie Souza
#Homework Assignment #2

import unittest
from Triangle import classify_triangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class test_triangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_righttrianglea(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def test_righttriangleb(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def test_equilateraltriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    #my test cases
    def test_equilateral1(self):
        self.assertEqual(classify_triangle(6,6,6), 'Equilateral', '6,6,6 is an Equilateral triangle')
    def test_isosceles(self):
        self.assertEqual(classify_triangle(9,9,5), 'Isosceles', '9,9,5 is an Isosceles Triangle')
    def test_icalene(self):
        self.assertEqual(classify_triangle(8,6,4), 'Scalene', '8,6,4 is a Scalene Triangle')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
