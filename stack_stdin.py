from check_type import *
import ast
import sys
import re

class StdIn():

	def __init__(self, inp_str):
		self.index = 0
		if len(inp_str) > 0:
			formatted_string = "[" + re.sub(r"\s+(?=([^\']*\'[^\']*\')*[^\']*$)", ", ", inp_str) + "]"
		else:
			formatted_string = "[]"
		self.list = ast.literal_eval(formatted_string)
		self.loop_counter = 0
		self.loop_level = 0
		self.loop_popped = False

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == len(self.list):
			self.index = 0
			raise StopIteration
		self.index += 1
		return self.list[self.index-1]

	def convert(self, item):
		if is_int_string(item):
			return int(item)
		elif is_float_string(item):
			return float(item)
		else:
			return ast.literal_eval(item)

	def set_loop_counter(self, counter, level):
		self.loop_counter = counter
		self.loop_level = level
		self.loop_popped = False

	def pop(self, expected_type = None):
		if self.loop_level > 0 and not self.loop_popped and expected_type == int:
			self.loop_popped = True
			return self.loop_counter
		elif self.list:
			ret = self.list[self.index]
			self.index = (self.index+1) % len(self.list)
			return ret
		elif expected_type == int:
			return 0
		elif expected_type == float:
			return 0
		elif expected_type == list:
			return []
		elif expected_type == str:
			return ""
		raise EOFError("No input has been provided")

class Stack():
	def __init__(self, lst):
		self.list = lst
		self.index = 0

	def __str__(self):
		return str(self.list)

	def __getitem__(self, index):
		return self.list[index]

	def __setitem__(self, index, value):
		self.list[index] = value

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == len(self.list):
			self.index = 0
			raise StopIteration
		self.index += 1
		return self.list[self.index-1]

	def append(self, item):
		self.list.append(item)

	def pop(self, operator, index = -1, expected_type = int):
		if self.list:
			if index < len(self.list) and -index <= len(self.list):
				return self.list.pop(index)
			else:
				return self.stdin.pop(expected_type)
		else:
			return self.stdin.pop(expected_type)
		raise IndexError("%s could not pop from stack" % operator)
