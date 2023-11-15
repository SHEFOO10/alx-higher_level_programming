#!/usr/bin/python3
""" Test Rectangle """
import io
import unittest
from models.rectangle import Rectangle
import os
import sys


class TestRectangle(unittest.TestCase):
	@staticmethod
	def capture_stdout(rect, method):
		"""Captures and returns text printed to stdout.

		Args:
			rect (Rectangle): The Rectangle to print to stdout.
			method (str): The method to run on rect.
		Returns:
			The text printed to stdout by calling method on sq.
		"""
		capture = io.StringIO()
		sys.stdout = capture
		if method == "print":
			print(rect)
		else:
			rect.display()
		sys.stdout = sys.__stdout__
		return capture

	def test_create_Rectangle(self):
		obj = Rectangle(1, 2)
		self.assertEqual(obj.width, 1)
		self.assertEqual(obj.height, 2)

	def test_create_Rectangle1(self):
		obj = Rectangle(1, 2, 3)
		self.assertEqual(obj.width, 1)
		self.assertEqual(obj.height, 2)
		self.assertEqual(obj.x, 3)

	def test_create_another_Rectangle2(self):
		obj = Rectangle(1, 2, 3, 4)
		self.assertEqual(obj.width, 1)
		self.assertEqual(obj.height, 2)
		self.assertEqual(obj.x, 3)
		self.assertEqual(obj.y, 4)

	def test_create_Rectangle_with_str_width(self):
		with self.assertRaises(TypeError):
			try:
				Rectangle('1', 2)
			except TypeError as e:
				self.assertEqual(e.__str__(), 'width must be an integer')
				raise

	def test_create_Rectangle_with_str_height(self):
		with self.assertRaises(TypeError):
			try:
				Rectangle(1, '2')
			except TypeError as e:
				self.assertEqual(e.__str__(), 'height must be an integer')
				raise

	def test_create_Rectangle_with_str_x(self):
		with self.assertRaises(TypeError):
			try:
				Rectangle(1, 2, '3')
			except TypeError as e:
				self.assertEqual(e.__str__(), 'x must be an integer')
				raise

	def test_create_Rectangle_with_str_y(self):
		with self.assertRaises(TypeError):
			try:
				Rectangle(1, 2, 3, '4')
			except TypeError as e:
				self.assertEqual(e.__str__(), 'y must be an integer')
				raise

	def test_create_normal_Rectangle(self):
		obj = Rectangle(1, 2, 3, 4, 5)
		self.assertEqual(obj.id, 5)

	def test_create_Rectangle_with_negative_width(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(-1, 2)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'width must be > 0')
				raise

	def test_create_Rectangle_with_negative_height(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(1, -2)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'height must be > 0')
				raise

	def test_create_Rectangle_with_0_width(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(0, 2)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'width must be > 0')
				raise

	def test_create_Rectangle_with_0_height(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(1, 0)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'height must be > 0')
				raise

	def test_create_Rectangle_with_negative_x(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(1, 2, -3)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'x must be >= 0')
				raise

	def test_create_Rectangle_with_negative_y(self):
		with self.assertRaises(ValueError):
			try:
				Rectangle(1, 2, 3, -4)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'y must be >= 0')
				raise
	def test_Rectangle_area(self):
		obj = Rectangle(3, 4)
		self.assertEqual(obj.area(), 12)

	def test_Rectangle_str(self):
		obj = Rectangle(1, 1)
		self.assertRegex(obj.__str__(), r"\[Rectangle\] \(\d+\) 0/0 - 1/1")

	def test_display(self):
		obj = Rectangle(2, 4)
		obj.display()
		self.assertEqual("##\n##\n##\n##\n", self.capture_stdout(obj, 'display').getvalue())


	def test_Rectangle_display_with_x(self):
		obj = Rectangle(2, 4, 2)
		obj.display()
		self.assertEqual("  ##\n  ##\n  ##\n  ##\n", self.capture_stdout(obj, 'display').getvalue())
	def test_Rectangle_to_dictionary(self):
		obj = Rectangle(2, 4)
		self.assertRegex(obj.to_json_string([obj.to_dictionary()]),
			r"[{'x': 0, 'y': 0, 'id': \d+, 'height': 4, 'width': 2}]")

	def test_Rectangle_update_nothing(self):
		obj = Rectangle(2, 4, 5, 9, 112)
		self.assertEqual(obj.to_dictionary(), {'height': 4, 'id': 112, 'width': 2, 'x': 5, 'y': 9})
		obj.update()
		self.assertEqual(obj.to_dictionary(), {'height': 4, 'id': 112, 'width': 2, 'x': 5, 'y': 9})

	def test_Rectangle_update(self):
		obj = Rectangle(2, 4, 5, 9, 112)
		self.assertEqual(obj.to_dictionary(), {'height': 4, 'id': 112, 'width': 2, 'x': 5, 'y': 9})
		obj.update(100, 3, 5, 10, 11)
		self.assertEqual(obj.to_dictionary(), {'height': 5, 'id': 100, 'width': 3, 'x': 10, 'y': 11})

	def test_Rectangle_update_id(self):
		obj = Rectangle(1, 3, 5, 9, 10)
		obj.update(98)
		self.assertEqual(obj.to_dictionary(), {'height': 3, 'id': 98, 'width': 1, 'x': 5, 'y': 9})

	def test_Rectangle_update_id_and_width(self):
		obj = Rectangle(10, 1)
		obj.update(98, 1)
		self.assertEqual(obj.to_dictionary(), {'height': 1, 'id': 98, 'width': 1, 'x': 0, 'y': 0})

	def test_Rectangle_update_id_width_height(self):
		obj = Rectangle(10, 10)
		obj.update(98, 1, 2)
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 98, 'width': 1, 'x': 0, 'y': 0})

	def test_Rectangle_update_id_width_height_x(self):
		obj = Rectangle(10, 10, 5)
		obj.update(98, 1, 2, 3)
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 98, 'width': 1, 'x': 3, 'y': 0})

	def test_Rectangle_update_id_width_height_x_y(self):
		obj = Rectangle(10, 10, 5, 10)
		obj.update(98, 1, 2, 3, 4)
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 98, 'width': 1, 'x': 3, 'y': 4})

	def test_Rectangle_update_id_width_with_kwargs(self):
		obj = Rectangle(5, 5)
		obj.update(**{ 'id': 89, 'width': 1 })
		self.assertEqual(obj.to_dictionary(), {'height': 5, 'id': 89, 'width': 1, 'x': 0, 'y': 0})

	def test_Rectangle_update_id_width_height_with_kwargs(self):
		obj = Rectangle(5, 5)
		obj.update(**{ 'id': 89, 'width': 1, 'height': 2})
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 89, 'width': 1, 'x': 0, 'y': 0})

	def test_Rectangle_update_id_width_height_x_with_kwargs(self):
		obj = Rectangle(5, 5)
		obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3})
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 89, 'width': 1, 'x': 3, 'y': 0})

	def test_Rectangle_update_id_width_height_x_with_kwargs(self):
		obj = Rectangle(5, 5)
		obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
		self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 89, 'width': 1, 'x': 3, 'y': 4})

	def test_Rectangle_save_to_file_None_value(self):
		Rectangle.save_to_file(None)
		self.assertTrue(os.path.exists('Rectangle.json'))
		with open('Rectangle.json') as f:
			self.assertEqual(f.read(), '[]')

	def test_Rectangle_save_file(self):
		Rectangle.save_to_file([])
		self.assertTrue(os.path.exists('Rectangle.json'))
		with open('Rectangle.json') as f:
			self.assertEqual(f.read(), '[]')

	def test_Rectangle_save_file_with_Rectangle(self):
		Rectangle.save_to_file([Rectangle(1, 2)])
		self.assertTrue(os.path.exists('Rectangle.json'))
		with open('Rectangle.json') as f:
			self.assertRegex(f.read(), r'[{"x": 0, "y": 0, "id": \d+, "height": 2, "width": 1}]')

	def test_Rectangle_load_from_file(self):
		objects = Rectangle.load_from_file()
		self.assertTrue(all(map(lambda obj: isinstance(obj, Rectangle), objects)))
