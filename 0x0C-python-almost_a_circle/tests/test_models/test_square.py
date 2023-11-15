#!/usr/bin/python3
""" Test Square Class """
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
	def test_create_square(self):
		obj = Square(1)
		self.assertEqual(obj.size, 1)

	def test_create_square_with_negative_size(self):
		with self.assertRaises(ValueError):
			try:
				obj = Square(-1)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'width must be > 0')
				raise

	def test_square_passing_x_with_the_size(self):
		obj = Square(1, 2)
		self.assertEqual(obj.x, 2)

	def test_square_passing_y_with_the_size(self):
		obj = Square(1, 2, 3)
		self.assertEqual(obj.y, 3)

	def test_square_pass_size_as_string(self):
		with self.assertRaises(TypeError):
			try:
				obj = Square("1")
			except TypeError as e:
				self.assertEqual(e.__str__(), 'width must be an integer')
				raise

	def test_square_pass_x_as_string(self):
		with self.assertRaises(TypeError):
			try:
				obj = Square(1, "2")
			except TypeError as e:
				self.assertEqual(e.__str__(), 'x must be an integer')
				raise

	def test_square_pass_y_as_string(self):
		with self.assertRaises(TypeError):
			try:
				obj = Square(1, 2, "3")
			except TypeError as e:
				self.assertEqual(e.__str__(), 'y must be an integer')
				raise

	def test_square_pass_negative_size(self):
		with self.assertRaises(ValueError):
			try:
				obj = Square(-1)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'width must be > 0')
				raise

	def test_square_pass_negative_x(self):
		with self.assertRaises(ValueError):
			try:
				obj = Square(1, -2)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'x must be >= 0')
				raise

	def test_square_pass_negative_y(self):
		with self.assertRaises(ValueError):
			try:
				obj = Square(1, 2, -3)
			except ValueError as e:
				self.assertEqual(e.__str__(), 'y must be >= 0')
				raise

	def test_square__str__(self):
		self.assertRegex(Square(1).__str__(), r"\[Square\] \(\d+\) 0/0 - 1")

	def test_square_to_dictionary(self):
		obj = Square(3, id=10)
		self.assertEqual(obj.to_dictionary(), {'id': 10, 'size': 3, 'x': 0, 'y': 0})

	def test_square_update_nothing(self):
		obj = Square(3, id=10)
		self.assertEqual(obj.to_dictionary(), {'id': 10, 'size': 3, 'x': 0, 'y': 0})
		obj.update()
		self.assertEqual(obj.to_dictionary(), {'id': 10, 'size': 3, 'x': 0, 'y': 0})

	def test_square_update_id(self):
		obj = Square(1)
		obj.update(89)
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

	def test_square_update_id_size(self):
		obj = Square(15)
		obj.update(89, 1)
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

	def test_square_update_id_size_x(self):
		obj = Square(15)
		obj.update(89, 1, 2)
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 0})

	def test_square_update_id_size_x_y(self):
		obj = Square(15)
		obj.update(89, 1, 2, 3)
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 3})

	def test_square_update_id_with_kwargs(self):
		obj = Square(1)
		obj.update(**{'id': 89})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})		

	def test_square_update_id_size_with_kwargs(self):
		obj = Square(5)
		obj.update(**{'id': 89, 'size': 1})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

	def test_square_update_id_size_x_with_kwargs(self):
		obj = Square(5)
		obj.update(**{'id': 89, 'size': 1, 'x': 2})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 0})

	def test_square_update_id_size_x_y_with_kwargs(self):
		obj = Square(5)
		obj.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 3})

	def test_square_create_with_id_from_dictionary(self):
		obj = Square.create(**{'id': 89})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

	def test_square_create_with_id_size_from_dictionary(self):
		obj = Square.create(**{'id': 89, 'size': 1})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 0, 'y': 0})

	def test_square_create_with_id_size_x_from_dictionary(self):
		obj = Square.create(**{'id': 89, 'size': 1, 'x': 2})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 0})

	def test_square_create_with_id_size_x_y_from_dictionary(self):
		obj = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
		self.assertEqual(obj.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 3})

	def test_square_save_to_file_with_None(self):
		Square.save_to_file(None)
		self.assertTrue(os.path.exists('Square.json'))
		with open('Square.json', 'r') as f:
			self.assertEqual(f.read(), '[]')

	def test_square_save_to_file(self):
		Square.save_to_file([])
		self.assertTrue(os.path.exists('Square.json'))
		with open('Square.json', 'r') as f:
			self.assertEqual(f.read(), '[]')

	def test_square_save_to_file(self):
		Square.save_to_file([Square(1)])
		self.assertTrue(os.path.exists('Square.json'))
		with open('Square.json', 'r') as f:
			self.assertRegex(f.read(), r'[{"id": \d+, "x": 0, "size": 1, "y": 0}]')

	def test_square_load_from_file(self):
		objects = Square.load_from_file()
		self.assertTrue(all(map(lambda obj: isinstance(obj, Square), objects)))
