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

Argument = namedtuple("Argument", ["char", "code"])
DEBUG = False

def evaluate(
	code,
	stdin,
	stack = Stack([]),
	level = 0,
	loop_counter = 0,
	loop_limit = 0,
	loop_value = None):

	stack.stdin = stdin

	zero_args = {
		"☻" : push_16,
		"♥" : push_32,
		"♦" : push_64,
		"♣" : push_128,
		"♠" : push_256,
		"•" : push_512,
		"◘" : push_1024,
		"○" : push_2048,
		"◙" : push_4096,
		"♂" : push_10,
		"♀" : push_100,
		"♪" : push_1000,
		"♫" : push_10000,
		"☼" : push_100000,
		"►" : push_1000000,
		"◄" : push_10000000,
		"↕" : push_100000000,
		"0" : push_0,
		"1" : push_1,
		"2" : push_2,
		"3" : push_3,
		"4" : push_4,
		"5" : push_5,
		"6" : push_6,
		"7" : push_7,
		"8" : push_8,
		"9" : push_9,
		"b" : push_neg1,
		"c" : push_neg2,
		"d" : push_neg3,
		"e" : push_e,
		"t" : push_unixtime,
		"v" : push_random_int,
		"⌂" : push_asterisk_yield,
		"ª" : push_1_array,
		"º" : push_0_array,
		"╟" : push_60,
		"╚" : push_3600,
		"╔" : push_86400,
		"π" : push_pi,
		"τ" : push_tau,
		" " : push_space,
		"A" : push_11,
		"B" : push_12,
		"C" : push_13,
		"D" : push_14,
		"E" : push_15,
		"F" : push_17,
		"G" : push_18,
		"H" : push_19,
		"I" : push_20,
		"J" : push_21,
		"K" : push_22,
		"L" : push_23,
		"M" : push_24,
		"N" : push_25,
		"O" : push_26,
		"P" : push_27,
		"Q" : push_28,
		"R" : push_29,
		"S" : push_30,
		"T" : push_31,
		"U" : push_33,
		"V" : push_34,
		"W" : push_35,
		"X" : push_36,
		"Y" : push_37,
		"Z" : push_38,
		"φ": golden_ratio_yield
	}

	one_arg = {
		"¶": is_prime_yield,
		"!": gamma_yield,
		"(": decrease_yield,
		")": increase_yield,
		";": discard_tos_yield,
		"a": wrap_in_array_yield,
		"f": fibonnaci_yield,
		"h": length_yield,
		"i": cast_to_integer_yield,
		"n": print_lines_yield,
		"o": print_without_popping_yield,
		"p": print_with_newline_yield,
		"q": print_without_newline_yield,
		"r": get_range_yield,
		"s": sort_list_or_string_yield,
		"w": get_random_value_yield,
		"x": reverse_value_yield,
		"y": join_list_without_separator_yield,
		"z": sort_list_or_string_reverse_yield,
		"à": to_binary_string_yield,
		"å": from_binary_string_yield,
		"â": to_binary_yield,
		"ä": from_binary_yield,
		"ç": is_truthy_filter_yield,
		"¢": convert_hexadecimal_yield,
		"£": length_with_pop_yield,
		"¥": modulo_2_yield,
		"ó": pow_2_yield,
		"ú": pow_10_yield,
		"ñ": palindromize_yield,
		"Ñ": check_palindrome_yield,
		"½": halve_yield,
		"¼": quarter_yield,
		"░": convert_to_string_yield,
		"▒": split_string_or_int_yield,
		"┤": pop_from_right_yield,
		"╡": discard_from_right_yield,
		"├": pop_from_left_yield,
		"╞": discard_from_left_yield,
		"┐": copy_and_decrease_yield,
		"└": copy_and_increase_yield,
		"┴": check_if_1_yield,
		"┬": check_if_0_yield,
		"─": flatten_or_get_divisors_yield,
		"╦": get_dictionary_words_yield,
		"╤": get_symmetric_range_yield,
		"╨": round_up_to_pow_2_yield,
		"╒": get_range_1_based_yield,
		"╥": round_down_to_pow_2_yield,
		"╫": left_rotate_yield,
		"╪": right_rotate_yield,
		"┘": to_boolean_yield,
		"┌": to_boolean_inverted_yield,
		"▀": get_unique_elements_yield,
		"Σ": get_sum_yield,
		"σ": remove_leading_zeroes_yield,
		"δ": capitalize_string_yield,
		"∞": double_element_yield,
		"⌠": increase_twice_yield,
		"⌡": decrease_twice_yield,
		"°": is_square_yield,
		"_": duplicate,
		"∙": triplicate,
		"·": quadruplicate,
		"√": get_sqrt_yield,
		"ⁿ": get_cube_yield,
		"²": get_square_yield,
		"■": get_self_product_or_collatz_yield
	}
	two_args = {
		"§": get_list_or_string_item_or_concatenate_yield,
		"+": add_yield,
		"-": subtract_yield,
		"*": mult_yield,
		"/": divide_yield,
		"#": power_yield,
		"u": join_yield,
		"▌": prepend_list_or_string_yield,
		"▐": append_list_or_string_yield,
		"Φ": increase_array_element_yield,
		"Θ": decrease_array_element_yield,
		"Ω": center_string_or_int_yield,
		"<": is_less,
		"=": is_equal,
		">": is_greater,
		"¡": is_not,
		"≥": is_geq,
		"≤": is_leq,
		"÷": is_divisible_yield,
		"%": modulo_yield,
		"═": pad_to_equal_length,
	}
	loop_handlers = {
		"↑": while_true_no_pop,
		"↓": while_false_no_pop,
		"→": while_true_pop,
		"←": while_false_pop,
		"∟" : do_while_true_no_pop,
		"↔" : do_while_false_no_pop,
		"▲" : do_while_true_pop,
		"▼" : do_while_false_pop
	}
	reducers = {
		"*": mult_yield,
		"#": power_yield,
		"+": add_yield,
		"-": subtract_yield,
		"/": divide_yield
	}

	loop_types = set("↑↓→←∟↔▲▼*")
	block_creators = set("ÄÅÉæÆ{ôöò")
	string_creators = set("ûùÿ╢╖╕╣║╗")
	string_terminators = set("\"«»")
	compressed_letters_0 = "etaoinsrdluczbfp"
	compressed_letters_1 = "gwymvkxjqh ?*#.,"

	words = resources.dictionary.words

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
			a = stack.pop(arg.char)
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

		elif arg.char == "?":
			if len(stack.list) < 3:
				raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			stack.append(stack.pop(arg.char, -3))
		elif arg.char == "@":
			if len(stack.list) < 3:
				raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			stack.append(stack.pop(arg.char, -3))
			stack.append(stack.pop(arg.char, -3))

		elif arg.char == "[":
			ret = evaluate(code, stdin, Stack([]), level+1, loop_counter, loop_limit, loop_value)
			stack.append(ret.list)
		elif arg.char == "\\":
			stack.append(stack.pop(arg.char, -2))
		elif arg.char == "]":
			if level > 0:
				return stack
			else:
				stack.list = [stack.list]

		elif arg.char == "g":
			op = code.pop()
			a = stack.pop(arg.char)
			if op.char in one_arg and is_list(a):
				stack.append([n for n in a if all(one_arg[op.char](n, op))])
			elif op.char in two_args:
				b = stack.pop(arg.char)
				if is_list(a) and is_num(b):
					stack.append([n for n in a if all(two_args[op.char](n, b, op))])
				elif is_num(a) and is_list(b):
					stack.append([n for n in b if all(two_args[op.char](a, n, op))])
				elif is_list(a) and is_list(b):
					if len(a) == len(b):
						stack.append([na for na, nb in zip(a, b) if all(two_args[op.char](na, nb, op))])
					else:
						raise ValueError("Both lists need to be of equal length for filtering")
			elif op.char in block_creators and is_list(a):
				c, code = create_block(op, code)
				stack.append([n for n in a if any(evaluate(c[:], stdin, Stack([n]), level+1))])
			else:
				raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op.char))

		elif arg.char == "j":
			a = float(stdin.pop())
			stack.append(a)
		elif arg.char == "k":
			a = int(stdin.pop())
			stack.append(a)
		elif arg.char == "l":
			a = stdin.pop()
			stack.append(a)

		elif arg.char == "m":
			op = code.pop()
			a = stack.pop(arg.char)
			if op.char in one_arg and is_list(a):
				stack.append([v for n in a for v in one_arg[op.char](n, op)])
			elif op.char in two_args:
				b = stack.pop(arg.char)
				if is_list(a) and is_num(b):
					stack.append([v for n in a for v in two_args[op.char](n, b, op)])
				elif is_num(a) and is_list(b):
					stack.append([v for n in b for v in two_args[op.char](a, n, op)])
				elif is_list(a) and is_list(b):
					if len(a) == len(b):
						stack.append([v for na, nb in zip(a, b) for v in two_args[op.char](na, nb, op)])
					else:
						raise ValueError("Both lists need to be of equal length for filtering")
			elif op.char in block_creators and is_list(a):
				c, code = create_block(op, code)
				stack.append([v for n in a for v in evaluate(c[:], stdin, Stack([n]), level+1)])
			else:
				raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op.char))

		elif arg.char == "á":
			a = stack.pop(arg.char)
			map_arg = code.pop()
			if map_arg.char in block_creators:
				map_block, code = create_block(map_arg, code)
			else:
				map_block = [map_arg]
			mapped = [evaluate(map_block[:], stdin, Stack([n]), level+1) for n in a]
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
				str_commands = [code_page.index(c)+1 for c in a]
				str_code_list = [Argument(char, c) for char, c in zip(a, str_commands)][::-1]
				stack = evaluate(str_code_list, stdin, stack, level+1)
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
			loop_type = code.pop() if code else Argument("*", 0)
			if loop_type.char not in loop_types:
				code.append(loop_type)
				loop_type = Argument("*", 0)
			if loop_type.char in loop_types:
				if loop_type.char == "*":
					limit = stack.pop(arg.char)
					if is_int(limit):
						loop_limit = limit
						for i in for_looping(limit):
							loop_counter = i
							stack = evaluate(c[:], stdin, stack, level+1, loop_counter, loop_limit)
					elif is_list(limit):
						loop_limit = len(limit)
						for i, n in enumerate(limit):
							loop_counter = i
							loop_value = n
							stack.append(loop_value)
							stack = evaluate(c[:], stdin, stack, level+1, loop_counter, loop_limit, loop_value)
				else:
					for i in loop_handlers[loop_type.char](stack):
						loop_counter = i
						stack = evaluate(c[:], stdin, stack, level+1, loop_counter)

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

		elif arg.char == "`":
			stack.append(stack[-2])
			stack.append(stack[-2])

		elif arg.char == " ":
			stack.list = [stack.pop(arg.char)]
		elif arg.char == "╘":
			stack.list = []
		else:
			raise ValueError("Not yet implemented: %s" % arg.char)
		if DEBUG:
			print(arg.char, stack)
			time.sleep(0.1)

	return stack

def print_list(l):
	return ''.join([str(s) if is_list(s) else str(s) for s in l])

def parse_input(byte_array):
	return ''.join([code_page[i] for i in list(byte_array)])

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('usage: python %s [-d] <code file>' % sys.argv[0])
		sys.exit(1)

	if sys.argv[1] == '-d':
		DEBUG = True
		sys.argv.pop(1)

	if sys.argv[1] == '--unittest':
		set_unittest()
		random.seed(1)
		sys.argv.pop(1)

	code_bytes = open(sys.argv[1], 'rb').read()
	code = parse_input(code_bytes)
	commands = [code_page.index(c)+1 for c in code]
	code_list = [Argument(char, c) for char, c in zip(code, commands)][::-1]
	stdin = StdIn("" if sys.stdin.isatty() else sys.stdin.read().rstrip("\n"))
	try:
		result = evaluate(code_list, stdin)
		print(print_list(result))
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print()
		print_exc()
		print("%s (line %d): %s" % (type(e).__name__, exc_tb.tb_lineno, e))
