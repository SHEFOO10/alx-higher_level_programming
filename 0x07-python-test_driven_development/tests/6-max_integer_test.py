#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	def test_list_is_empty(self):
		self.assertEqual(max_integer(), None)

	def test_one_element_list(self):
		self.assertEqual(max_integer([2]), 2)

	def test_max_at_the_begining(self):
		self.assertEqual(max_integer([5, 3, 2, 1]), 5)

	def test_max_at_the_end(self):
		self.assertEqual(max_integer([4, 3, 2, 6]), 6)

	def test_max_in_the_middle(self):
		self.assertEqual(max_integer([1, 3, 2, 100, 10, 5, 0]), 100)

	def test_one_negative_number(self):
		self.assertEqual(max_integer([2, -3, 20, 23, -7, 5]), 23)

	def test_negative_numbers(self):
		self.assertEqual(max_integer([-3, -2, -7, -1, -9]), -1)