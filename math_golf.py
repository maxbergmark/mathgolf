import math
import sys
from collections import namedtuple
import time
import itertools
import random
import resources.dictionary
from traceback import print_exc, format_exc
from functools import reduce

from code_page import *
from helper_functions import *
from stack_stdin import *
from two_arguments import *
from single_argument import *
from zero_arguments import *
from check_type import *
from function_delegates import *

Argument = namedtuple("Argument", ["char", "code"])
DEBUG = False
SLOW = False

global loop_counter
global loop_limit
global loop_value
global loop_level
loop_counter = 0
loop_limit = 0
loop_value = None
loop_level = 0

loop_types = set("↑↓→←∟↔▲▼*↨")
block_creators = set("ÄÅÉæÆ{ôöò")
string_creators = set("ûùÿ╢╖╕╣║╗")
string_terminators = set("\"«»")
compressed_letters_0 = "etaoinsrdluczbfp"
compressed_letters_1 = "gwymvkxjqh ?*#.,"

def evaluate(
	code,
	stdin,
	stack,
	level = 0):

	stack.stdin = stdin

	words = resources.dictionary.words
	global loop_counter
	global loop_limit
	global loop_value
	global loop_level

	while code:
		arg = code.pop()

		if arg.char in zero_args:
			for val in zero_args[arg.char](arg):
				stack.append(val)

		elif arg.char in one_arg:
			a = stack.pop(arg.char)
			for val in one_arg[arg.char](a, arg):
				stack.append(val)

		elif arg.char in two_args:
			b = stack.pop(arg.char)
			a = stack.pop(arg.char, -1, type(b))
			for val in two_args[arg.char](a, b, arg):
				stack.append(val)

		elif arg.char == "\"":
			s = ""
			c = "" if not code else code.pop().char
			while c not in  string_terminators and code:
				if c == "\\":
					s += code.pop().char
				else:
					s += c
				c = code.pop().char
			if not code and c not in string_terminators:
				s += c
				stack.append(s)
			elif c == "\"":
				stack.append(s)
			else:
				if c == "«":
					compressed = "etaoinsrhluczbfp"
				elif c == "»":
					compressed = "gwymvkxjqd_?*#.,"

				stack.append(decompress(s, compressed))

		elif arg.char in string_creators:
			s = ""
			if arg.char in "╢╣":
				s += code.pop().char
			elif arg.char in "û╖║╕╗":
				s += code.pop().char
				s += code.pop().char
			elif arg.char == "ù":
				s += code.pop().char
				s += code.pop().char
				s += code.pop().char
			elif arg.char == "ÿ":
				s += code.pop().char
				s += code.pop().char
				s += code.pop().char
				s += code.pop().char
			if arg.char in  "╢╖╕":
				s = decompress(s, compressed_letters_0)
			elif arg.char in "╣║╗":
				s = decompress(s, compressed_letters_1)
			if arg.char in "╖║":
				s = s[:3]
			stack.append(s)

		elif arg.char == "'":
			stack.append(code.pop().char)

		elif arg.char == "‼":
			arg_0 = code.pop()
			arg_1 = code.pop()
			arg_0_correct = (arg_0.char in one_arg or arg_0.char in two_args)
			arg_1_correct = (arg_1.char in one_arg or arg_1.char in two_args)
			should_pop_2 = (arg_0.char in two_args or arg_1.char in two_args)
			if not (arg_0_correct and arg_1_correct):
				raise ValueError("%s%s%s is not supported" % (arg.char, arg_0.char, arg_1.char))
			elif should_pop_2:
				b = stack.pop(arg.char)
				a = stack.pop(arg.char, -1, type(b))
				if arg_0.char in two_args:
					for val in two_args[arg_0.char](a, b, arg_0):
						stack.append(val)
				else:
					for val in one_arg[arg_0.char](a, arg_0):
						stack.append(val)

				if arg_1.char in two_args:
					for val in two_args[arg_1.char](a, b, arg_1):
						stack.append(val)
				else:
					for val in one_arg[arg_1.char](a, arg_1):
						stack.append(val)
			else:
				a = stack.pop(arg.char)
				for val in one_arg[arg_0.char](a, arg_0):
					stack.append(val)
				for val in one_arg[arg_1.char](a, arg_1):
					stack.append(val)


		elif arg.char == "?":
			c = stack.pop(arg.char)
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append(b)
			stack.append(c)
			stack.append(a)
			# if len(stack.list) < 3:
				# raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			# stack.append(stack.pop(arg.char, -3))
		elif arg.char == "@":
			c = stack.pop(arg.char)
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append(c)
			stack.append(a)
			stack.append(b)
			# if len(stack.list) < 3:
				# raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			# stack.append(stack.pop(arg.char, -3))
			# stack.append(stack.pop(arg.char, -3))

		elif arg.char == "[":
			ret = evaluate(code, stdin, Stack([]), level+1)
			stack.append(ret.list)
		elif arg.char == "\\":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append(b)
			stack.append(a)
			# stack.append(stack.pop(arg.char, -2))
		elif arg.char == "]":
			if level > 0:
				return stack
			else:
				stack.list = [stack.list]

		elif arg.char == "g":
			code = filter_list_or_string(code, stdin, stack, level, arg)
		elif arg.char == "Ç":
			code = inverted_filter_list_or_string(code, stdin, stack, level, arg)

		elif arg.char == "j":
			a = float(stdin.pop())
			stack.append(a)
		elif arg.char == "k":
			a = int(stdin.pop())
			stack.append(a)
		elif arg.char == "l":
			a = str(stdin.pop())
			stack.append(a)

		elif arg.char == "m":
			code = map_list_or_string(code, stdin, stack, level, arg)

		elif arg.char == "á":
			a = stack.pop(arg.char)
			map_arg = code.pop()
			if map_arg.char in block_creators:
				map_block, code = create_block(map_arg, code)
			else:
				map_block = [map_arg]
			loop_level += 1
			mapped = [evaluate(map_block[:], stdin, Stack([n]), level+1) for n in a]
			loop_level -= 1
			b = [n[1] for n in sorted(enumerate(a), key=lambda v:mapped[v[0]][0])]
			if is_str(a):
				stack.append(''.join(b))
			else:
				stack.append(b)

		elif arg.char == "~":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(~a)
			elif is_list(a):
				[stack.append(n) for n in a]
			elif is_str(a):
				str_commands = [code_page.index(c) for c in a]
				str_code_list = [Argument(char, c) for char, c in zip(a, str_commands)][::-1]
				stack.list = evaluate(str_code_list, stdin, stack, level+1).list
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ê":
			stack.append([int(i) for i in stdin])
		elif arg.char == "ë":
			stack.append([float(i) for i in stdin])
		elif arg.char == "è":
			stack.append([str(i) for i in stdin])

		elif arg.char == "ï":
			stack.append(loop_counter)
		elif arg.char == "î":
			stack.append(loop_counter+1)
		elif arg.char == "ì":
			stack.append(loop_value)
		elif arg.char == "í":
			stack.append(loop_limit)

		elif arg.char in block_creators:
			c, code = create_block(arg, code)
			# print(c, code)
			loop_type = code.pop() if code else Argument("*", 0)
			if loop_type.char not in loop_types:
				code.append(loop_type)
				loop_type = Argument("*", 0)
			if loop_type.char in loop_types:
				if loop_type.char == "*":
					limit = stack.pop(arg.char)
					if is_int(limit):
						loop_limit = limit
						loop_level += 1
						for i in for_looping(limit):
							loop_counter = i
							stdin.set_loop_counter(loop_counter, loop_level)
							stack = evaluate(c[:], stdin, stack, level+1)
						loop_level -= 1
					elif is_list(limit):
						loop_limit = len(limit)
						loop_level += 1
						for i, n in enumerate(limit):
							loop_counter = i
							stdin.set_loop_counter(loop_counter, loop_level)
							loop_value = n
							stack.append(loop_value)
							stack = evaluate(c[:], stdin, stack, level+1)
						loop_level -= 1
					elif is_str(limit):
						loop_limit = len(limit)
						loop_level += 1
						for i, n in enumerate(limit):
							loop_counter = i
							stdin.set_loop_counter(loop_counter, loop_level)
							loop_value = n
							stack.append(loop_value)
							stack = evaluate(c[:], stdin, stack, level+1)
						loop_level -= 1
					else:
						raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
				elif loop_type.char == "↨":
					limit_0 = stack.pop(arg.char)
					limit_1 = stack.pop(arg.char)
					if is_int(limit_0) and is_int(limit_1):
						if limit_0 <= limit_1:
							loop_limit = limit_1+1
							loop_level += 1
							for i in range(limit_0, limit_1+1):
								loop_counter = i
								stdin.set_loop_counter(loop_counter, loop_level)
								stack = evaluate(c[:], stdin, stack, level+1)
							loop_level -= 1
						else:
							loop_limit = limit_1
							loop_level += 1
							for i in range(limit_0, limit_1-1, -1):
								loop_counter = i
								stdin.set_loop_counter(loop_counter, loop_level)
								stack = evaluate(c[:], stdin, stack, level+1)
							loop_level -= 1
					else:
						raise ValueError("[%s][%s]%s is not supported" % (type(a),type(b),arg.char))
				else:
					for i in loop_handlers[loop_type.char](stack):
						loop_counter = i
						stdin.set_loop_counter(loop_counter, loop_level)
						stack = evaluate(c[:], stdin, stack, level+1)

		elif arg.char == "¿":
			a = stack.pop(arg.char)

			truth_arg = code.pop()
			if truth_arg.char in block_creators:
				truth_block, code = create_block(truth_arg, code)
			else:
				truth_block = [truth_arg]

			false_arg = code.pop()
			if false_arg.char in block_creators:
				false_block, code = create_block(false_arg, code)
			else:
				false_block = [false_arg]

			if is_truthy(a):
				code += truth_block
			else:
				code += false_block

		elif arg.char == "╜":
			a = stack.pop(arg.char)

			false_arg = code.pop()
			if false_arg.char in block_creators:
				false_block, code = create_block(false_arg, code)
			else:
				false_block = [false_arg]

			if is_falsey(a):
				code += false_block

		elif arg.char == "╛":
			a = stack.pop(arg.char)
			truth_arg = code.pop()
			if truth_arg.char in block_creators:
				truth_block, code = create_block(truth_arg, code)
			else:
				truth_block = [truth_arg]

			if is_truthy(a):
				code += truth_block

		elif arg.char == "⌐":
			stack.append(stack.pop(arg.char, 0))

		elif arg.char == "¬":
			stack.list = [stack.pop(arg.char)] + stack.list

		elif arg.char == "╩":
			next_char = code.pop().code
			stack.append(words[next_char])

		elif arg.char == "╙":
			a = stack.pop(arg.char)
			if is_num(a):
				b = stack.pop(arg.char)
				if is_num(b):
					stack.append(max(a, b))
				else:
					raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
			elif is_str(a):
				b = stack.pop(arg.char)
				if is_str(b):
					stack.append(max(a, b))
				else:
					raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
			if is_list(a):
				if len(a) > 0:
					stack.append(max(a))

		elif arg.char == "╓":
			a = stack.pop(arg.char)
			if is_num(a):
				b = stack.pop(arg.char)
				if is_num(b):
					stack.append(min(a, b))
				else:
					raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
			elif is_str(a):
				b = stack.pop(arg.char)
				if is_str(b):
					stack.append(min(a, b))
				else:
					raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
			if is_list(a):
				if len(a) > 0:
					stack.append(min(a))

		elif arg.char == "α":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append([a, b])

		elif arg.char == "ß":
			c = stack.pop(arg.char)
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append([a, b, c])

		elif arg.char == "Γ":
			d = stack.pop(arg.char)
			c = stack.pop(arg.char)
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append([a, b, c, d])

		elif arg.char == "µ":
			c = stack.pop(arg.char)
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_int(a) and is_int(b) and is_list(c):
				c[a], c[b] = c[b], c[a]
				stack.append(c)
			elif is_int(a) and is_list(b) and is_int(c):
				b[a], b[c] = b[c], b[a]
				stack.append(b)
			elif is_list(a) and is_int(b) and is_int(c):
				a[b], a[c] = a[c], a[b]
				stack.append(a)
			elif is_int(a) and is_int(b) and is_str(c):
				tmp = list(c)
				tmp[a], tmp[b] = tmp[b], tmp[a]
				c = ''.join(tmp)
				stack.append(c)
			elif is_int(a) and is_str(b) and is_int(c):
				tmp = list(b)
				tmp[a], tmp[c] = tmp[c], tmp[a]
				b = ''.join(tmp)
				stack.append(b)
			elif is_str(a) and is_int(b) and is_int(c):
				tmp = list(a)
				tmp[b], tmp[c] = tmp[c], tmp[b]
				a = ''.join(tmp)
				stack.append(a)
			else:
				raise ValueError("[%s][%s][%s]%s is not supported" % (type(a), type(b), type(c),arg.char))

		elif arg.char == "ε":
			a = stack.pop(arg.char)
			if is_list(a):
				op = code.pop()
				if op.char in reducers:
					value = a[0] if a else 0
					for n in a[1:]:
						for step in reducers[op.char](value, n, op):
							value = step
					stack.append(value)
				else:
					raise ValueError("[%s]%s%s is not a valid reduction" % (a, arg.char, operator))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "┼":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append(a)
			stack.append(b)
			stack.append(a)

		elif arg.char == "`":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			stack.append(a)
			stack.append(b)
			stack.append(a)
			stack.append(b)

		elif arg.char == "Þ":
			stack.list = [stack.pop(arg.char)]

		elif arg.char == "╘":
			stack.list = []

		else:
			raise ValueError("Not yet implemented: %s" % arg.char)

		if DEBUG:
			print(arg.char, stack, file=sys.stderr)
			if SLOW:
				time.sleep(0.1)

	return stack

def filter_list_or_string(code, stdin, stack, level, arg):

	global loop_counter
	global loop_limit
	global loop_value
	global loop_level

	op = code.pop()
	a = stack.pop(arg.char)
	if op.char in one_arg:
		if is_list(a):
			stack.append([n for n in a if all(one_arg[op.char](n, op))])
		elif is_str(a):
			stack.append(''.join([n for n in a if all(one_arg[op.char](n, op))]))
	elif op.char in two_args:
		b = stack.pop(arg.char)
		if is_list(a) and is_num(b):
			stack.append([n for n in a if all(two_args[op.char](n, b, op))])
		elif is_num(a) and is_list(b):
			stack.append([n for n in b if all(two_args[op.char](a, n, op))])
		elif is_str(a) and is_num(b):
			stack.append(''.join([n for n in a if all(two_args[op.char](n, b, op))]))
		elif is_num(a) and is_str(b):
			stack.append(''.join([n for n in b if all(two_args[op.char](a, n, op))]))
		elif is_list(a) and is_list(b):
			if len(a) == len(b):
				stack.append([na for na, nb in zip(a, b) if all(two_args[op.char](na, nb, op))])
			else:
				raise ValueError("Both lists need to be of equal length for filtering")
		elif is_str(a) and is_str(b):
			if len(a) == len(b):
				stack.append(''.join([na for na, nb in zip(a, b) if all(two_args[op.char](na, nb, op))]))
			else:
				raise ValueError("Both strings need to be of equal length for filtering")
	elif op.char in block_creators and is_list(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			if any(evaluate(c[:], stdin, Stack([n]), level+1)):
				res.append(n)
		loop_level -= 1
		stack.append(res)

	elif op.char in block_creators and is_str(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			if any(evaluate(c[:], stdin, Stack([n]), level+1)):
				res.append(n)
		loop_level -= 1
		stack.append(''.join(res))
	else:
		raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op.char))
	return code

def inverted_filter_list_or_string(code, stdin, stack, level, arg):

	global loop_counter
	global loop_limit
	global loop_value
	global loop_level

	op = code.pop()
	a = stack.pop(arg.char)
	if op.char in one_arg:
		if is_list(a):
			stack.append([n for n in a if not all(one_arg[op.char](n, op))])
		elif is_str(a):
			stack.append(''.join([n for n in a if not all(one_arg[op.char](n, op))]))
	elif op.char in two_args:
		b = stack.pop(arg.char)
		if is_list(a) and is_num(b):
			stack.append([n for n in a if not all(two_args[op.char](n, b, op))])
		elif is_num(a) and is_list(b):
			stack.append([n for n in b if not all(two_args[op.char](a, n, op))])
		elif is_str(a) and is_num(b):
			stack.append(''.join([n for n in a if not all(two_args[op.char](n, b, op))]))
		elif is_num(a) and is_str(b):
			stack.append(''.join([n for n in b if not all(two_args[op.char](a, n, op))]))
		elif is_list(a) and is_list(b):
			if len(a) == len(b):
				stack.append([na for na, nb in zip(a, b) if not all(two_args[op.char](na, nb, op))])
			else:
				raise ValueError("Both lists need to be of equal length for filtering")
		elif is_str(a) and is_str(b):
			if len(a) == len(b):
				stack.append(''.join([na for na, nb in zip(a, b) if not all(two_args[op.char](na, nb, op))]))
			else:
				raise ValueError("Both strings need to be of equal length for filtering")
	elif op.char in block_creators and is_list(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			if not any(evaluate(c[:], stdin, Stack([n]), level+1)):
				res.append(n)
		loop_level -= 1
		stack.append(res)

	elif op.char in block_creators and is_str(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			if not any(evaluate(c[:], stdin, Stack([n]), level+1)):
				res.append(n)
		loop_level -= 1
		stack.append(''.join(res))
	else:
		raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op.char))
	return code

def map_list_or_string(code, stdin, stack, level, arg):

	global loop_counter
	global loop_limit
	global loop_value
	global loop_level

	op = code.pop()
	a = stack.pop(arg.char)
	if op.char in one_arg:
		if is_list(a):
			stack.append([v for n in a for v in one_arg[op.char](n, op)])
		elif is_str(a):
			stack.append(''.join([v for n in a for v in one_arg[op.char](n, op)]))
	elif op.char in two_args:
		b = stack.pop(arg.char)
		if is_list(a) and is_num(b):
			stack.append([v for n in a for v in two_args[op.char](n, b, op)])
		elif is_num(a) and is_list(b):
			stack.append([v for n in b for v in two_args[op.char](a, n, op)])
		elif is_str(a) and is_num(b):
			stack.append(''.join([v for n in a for v in two_args[op.char](n, b, op)]))
		elif is_num(a) and is_str(b):
			stack.append(''.join([v for n in b for v in two_args[op.char](a, n, op)]))
		elif is_list(a) and is_list(b):
			if len(a) == len(b):
				stack.append([v for na, nb in zip(a, b) for v in two_args[op.char](na, nb, op)])
			else:
				raise ValueError("Both lists need to be of equal length for filtering")
		elif is_str(a) and is_str(b):
			if len(a) == len(b):
				stack.append(''.join([v for na, nb in zip(a, b) for v in two_args[op.char](na, nb, op)]))
			else:
				raise ValueError("Both strings need to be of equal length for filtering")
	elif op.char in block_creators and is_list(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			for v in evaluate(c[:], stdin, Stack([n]), level+1):
				res.append(v)
		loop_level -= 1
		stack.append(res)

	elif op.char in block_creators and is_str(a):
		c, code = create_block(op, code)
		res = []
		loop_level += 1
		for i, n in enumerate(a):
			loop_counter = i
			stdin.set_loop_counter(loop_counter, loop_level)
			loop_limit = len(a)
			loop_value = n
			for v in evaluate(c[:], stdin, Stack([n]), level+1):
				res.append(str(v))
		loop_level -= 1
		stack.append(''.join(res))
	else:
		raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op.char))
	return code


def print_list(l):
	return ''.join([str(s) if is_list(s) else str(s) for s in l])

def parse_input(byte_array):
	return ''.join([code_page[i] for i in list(byte_array)])

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('usage: python %s [-d] <code file>' % sys.argv[0])
		sys.exit(1)

	if '-d' in sys.argv:
		DEBUG = True
		sys.argv.remove('-d')

	if '-s' in sys.argv:
		SLOW = True
		sys.argv.remove('-s')

	if '-e' in sys.argv:
		code_bytes = open(sys.argv[1], 'rb').read()
		code = parse_input(code_bytes)
		from create_explanation import *
		create_explanation(code)
		quit()

	if '--unittest' in sys.argv:
		set_unittest()
		random.seed(1)
		sys.argv.remove('--unittest')

	code_bytes = open(sys.argv[1], 'rb').read()
	code = parse_input(code_bytes)
	commands = [code_page.index(c) for c in code]
	code_list = [Argument(char, c) for char, c in zip(code, commands)][::-1]
	input_lines = [""] if sys.stdin.isatty() else sys.stdin.read().rstrip("\n").split("\n")

	for i, line in enumerate(input_lines):
		try:
			stdin = StdIn(line)
			result = evaluate(code_list[:], stdin, Stack([]))
			print(print_list(result), end = '\n' if i<len(input_lines)-1 else '')
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print()
			print_exc()
			print("%s (line %d): %s" % (type(e).__name__, exc_tb.tb_lineno, e))
