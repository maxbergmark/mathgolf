from check_type import *
import ast
import sys

class StdIn():

	def __init__(self, lst):
		self.index = 0
		self.list = lst

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == len(self.list):
			self.index = 0
			raise StopIteration
		self.index += 1
		return self.convert(self.list[self.index-1])

	def convert(self, item):
		# print(item, file=sys.stderr)
		if is_int_string(item):
			return int(item)
		elif is_float_string(item):
			return float(item)
		else:
			return ast.literal_eval(item)

	def pop(self):
		if self.list:
			ret = self.list[self.index]
			self.index = (self.index+1) % len(self.list)
			return self.convert(ret)
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

	def pop(self, operator, index = -1):
		if self.list:
			return self.list.pop(index)
		else:
			return self.stdin.pop()
		raise IndexError("%s could not pop from stack" % operator)