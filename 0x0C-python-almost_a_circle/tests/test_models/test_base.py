#!/usr/bin/python3
"""
0. If it's not tested it doesn't work
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

	def test_autoId(self):
		obj = Base()
		self.assertEqual(obj.id, 1)
		obj2 = Base()
		self.assertEqual(obj2.id, 2)

	def test_passId(self):
		obj = Base(89)
		self.assertEqual(obj.id, 89)

	def test_jsonstring_with_None(self):
		self.assertEqual(Base.to_json_string(None), '[]')

	def test_jsonstring_with_empty_list(self):
		self.assertEqual(Base.to_json_string([]), '[]')

	def test_dictionary_to_jsonstring(self):
		self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

	def test_from_jsonstring_with_None(self):
		self.assertEqual(Base.from_json_string(None), [])

	def test_from_jsonstring_with_empty_list(self):
		self.assertEqual(Base.from_json_string('[]'), [])

	def test_from_jsonstring_to_listOfdictionaries(self):
		self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{ "id": 89 }])
