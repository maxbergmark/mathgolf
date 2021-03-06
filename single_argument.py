from check_type import *
import math
import random
import resources.dictionary
import itertools
from helper_functions import *

words = resources.dictionary.words

def fibonnaci(n):
	a, b = 0, 1
	for i in range(n//2):
		a, b = a+b, a+2*b
	return [a, b][n%2]

def fibonnaci_yield(a, arg):
	if is_int(a):
		yield fibonnaci(a)
	elif is_list(a):
		yield [fibonnaci(n) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def length_yield(a, arg):
	yield a
	if is_int(a):
		yield len(str(a))
	elif is_list(a):
		yield len(a)
	elif is_str(a):
		yield len(a)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def cast_to_integer_yield(a, arg):
	if is_list(a):
		yield [int(n) if is_num(n) or is_int_string(n) else n for n in a]
	elif is_num(a):
		yield int(a)
	elif is_str(a):
		yield int(a)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_range_yield(a, arg):
	if is_int(a):
		yield list(range(a))
	elif is_num(a):
		yield list(range(int(a)))
	elif is_list(a):
		yield [list(range(n)) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def sort_list_or_string_yield(a, arg):
	if is_list(a):
		yield sorted(a)
	elif is_str(a):
		yield ''.join(sorted(a))
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def sort_list_or_string_reverse_yield(a, arg):
	for val in sort_list_or_string_yield(a, arg):
		yield val[::-1]

def get_random_value_yield(a, arg):
	if is_int(a):
		yield random.randint(0, a)
	elif is_list(a):
		yield random.choice(a)
	elif is_str(a):
		yield random.choice(a)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def reverse_value_yield(a, arg):
	if is_int(a):
		yield int(str(a)[::-1])
	elif is_list(a):
		yield a[::-1]
	elif is_str(a):
		yield a[::-1]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def modulo_2_yield(a, arg):
	if is_num(a):
		yield a % 2
	elif is_list(a):
		yield [n % 2 for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def pow_2_yield(a, arg):
	if is_int(a):
		yield 2**a
	elif is_num(a):
		yield 2**a
	elif is_list(a):
		yield [2**n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def pow_10_yield(a, arg):
	if is_int(a):
		yield int(10**a)
	elif is_num(a):
		yield 10**a
	elif is_list(a):
		yield [10**n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def palindromize_yield(a, arg):
	if is_int(a):
		a = str(a)
		yield int(a+a[::-1][1:])
	elif is_list(a):
		yield a+a[::-1][1:]
	elif is_str(a):
		yield a+a[::-1][1:]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def check_palindrome_yield(a, arg):
	if is_int(a):
		a = str(a)
		yield int(a == a[::-1])
	elif is_list(a):
		yield int(a == a[::-1])
	elif is_str(a):
		yield int(a == a[::-1])
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def halve_yield(a, arg):
	if is_num(a):
		if is_int(a):
			yield a//2
		else:
			yield a/2
	elif is_str(a):
		yield a[::2]
		yield a[1::2]
	elif is_list(a):
		yield [n for b in a for n in halve_yield(b, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def quarter_yield(a, arg):
	if is_num(a):
		if is_int(a):
			yield a//4
		else:
			yield a/4
	elif is_str(a):
		yield a[:len(a)//2]
	elif is_list(a):
		yield a[:len(a)//2]
		# yield [n//4 if is_int(n) else n/4 for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def convert_to_string_yield(a, arg):
	if is_num(a):
		yield str(a)
	elif is_list(a):
		yield [str(n) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def split_string_or_int_yield(a, arg):
	if is_int(a):
		yield [int(n) for n in str(a)]
	elif is_str(a):
		yield list(a)
	elif is_list(a):
		yield 2*a
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def pop_from_right_yield(a, arg):
	if is_str(a):
		yield a[:-1]
		yield a[-1]
	elif is_list(a):
		yield a[:-1]
		yield a[-1]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def discard_from_right_yield(a, arg):
	if is_str(a):
		yield a[:-1]
	elif is_list(a):
		yield a[:-1]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def pop_from_left_yield(a, arg):
	if is_str(a):
		yield a[1:]
		yield a[0]
	elif is_list(a):
		yield a[1:]
		yield a[0]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def discard_from_left_yield(a, arg):
	if is_str(a):
		yield a[1:]
	elif is_list(a):
		yield a[1:]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def copy_and_decrease_yield(a, arg):
	if is_num(a):
		yield a
		yield a-1
	elif is_str(a):
		if len(a) == 1:
			yield a
			yield chr(ord(a)-1)
		else:
			yield a
			for res in decrease_yield(a, arg):
				yield res
	elif is_list(a):
		yield [v for n in a for v in copy_and_decrease_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def copy_and_increase_yield(a, arg):
	if is_num(a):
		yield a
		yield a+1
	elif is_str(a):
		if len(a) == 1:
			yield a
			yield chr(ord(a)+1)
		else:
			yield a
			for res in increase_yield(a, arg):
				yield res
	elif is_list(a):
		yield [v for n in a for v in copy_and_increase_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def check_if_1_yield(a, arg):
	if is_num(a):
		yield int(a == 1)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def check_if_0_yield(a, arg):
	if is_num(a):
		yield int(a == 0)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_dictionary_words_yield(a, arg):
	if is_int(a):
		yield words[a % len(words)]
	elif is_str(a):
		idx = char_to_ord(a)
		yield words[idx % len(words)]
	elif is_list(a):
		yield [v for n in a for v in get_dictionary_words_yield(n, arg)]
		# yield [words[n] if is_int(n) else n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def flatten_or_get_divisors_yield(a, arg):
	if is_int(a):
		yield [n for n in range(1, a+1) if a%n == 0]
	elif is_list(a):
		res = [n for b in a for n in flatten_yield(b, arg)]
		# print(res)
		yield res
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def flatten_yield(a, arg):
	# print(a)
	if is_list(a):
		for v in [n for b in a for n in flatten_yield(b, arg)]:
			yield v
	else:
		yield a

def get_symmetric_range_yield(a, arg):
	if is_num(a):
		yield list(range(-int(a), int(a)+1))
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def round_up_to_pow_2_yield(a, arg):
	if is_num(a):
		if a == 0:
			yield 0
		elif a > 0:
			yield 2**int(math.log(a, 2)+1)
		else:
			for val in round_up_to_pow_2_yield(-a, arg):
				yield val
	elif is_list(a):
		yield [v for n in a for v in round_up_to_pow_2_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def round_down_to_pow_2_yield(a, arg):
	if is_num(a):
		if a == 0:
			yield 0
		elif a > 0:
			yield 2**int(math.log(a, 2))
		else:
			for val in round_down_to_pow_2_yield(-a, arg):
				yield val
	elif is_list(a):
		yield [v for n in a for v in round_down_to_pow_2_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_range_1_based_yield(a, arg):
	if is_num(a):
		yield list(range(1, int(a)+1))
	elif is_list(a):
		yield [list(range(1, n+1)) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def left_rotate_yield(a, arg):
	if is_int(a):
		yield int(bin(a)[3:]+'1', 2)
	elif is_list(a):
		yield a[1:] + [a[0]]
	elif is_str(a):
		yield a[1:] + a[0]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def right_rotate_yield(a, arg):
	if is_int(a):
		yield int(str(a&1)+bin(a)[2:-1], 2)
	elif is_list(a):
		yield [a[-1]] + a[:-1]
	elif is_str(a):
		yield a[-1] + a[:-1]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def to_boolean_yield(a, arg):
	if is_num(a):
		yield int(is_truthy(a))
	elif is_str(a):
		yield int(is_truthy(a))
	elif is_list(a):
		yield [int(is_truthy(n)) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def to_boolean_inverted_yield(a, arg):
	if is_num(a):
		yield int(is_falsey(a))
	elif is_str(a):
		yield int(is_falsey(a))
	elif is_list(a):
		yield [int(is_falsey(n)) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_unique_elements_yield(a, arg):
	if is_str(a):
		b = []
		for n in a:
			if n not in b:
				b.append(n)
		yield ''.join(b)
	elif is_list(a):
		b = []
		for n in a:
			if n not in b:
				b.append(n)
		yield b
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_sum_yield(a, arg):
	if is_int(a):
		yield sum(int(d) for d in str(a))
	elif is_list(a):
		if len(a) > 0 and is_int(a[0]):
			yield sum(a)
		elif len(a) > 0 and is_num(a[0]):
			yield sum(a)
		elif len(a) > 0 and is_str(a[0]):
			yield ''.join([str(n) for n in a])
		elif len(a) > 0 and is_list(a[0]):
			s = 0
			for element in a:
				for res in get_sum_yield(element, arg):
					s += res
			yield s
		else:
			yield 0
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def remove_leading_zeroes_yield(a, arg):
	if is_int(a):
		yield 0 if a == 0 else a // abs(a)
	elif is_num(a):
		yield 0 if a == 0 else a / abs(a)
	elif is_str(a):
		yield a.lstrip("0")
	elif is_list(a):
		if len(a) > 0 and is_int(a[0]):
			yield ["" if n == 0 else str(n) for n in a]
		elif len(a) > 0 and is_str(a[0]):
			yield [n.lstrip("0") for n in a]
		else:
			yield []
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def capitalize_string_yield(a, arg):
	if is_str(a):
		yield a.capitalize()
	elif is_list(a):
		yield [n.capitalize() if is_str(n) else n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def double_element_yield(a, arg):
	if is_num(a):
		yield a*2
	elif is_str(a):
		yield a*2
	elif is_list(a):
		yield [b for n in a for b in double_element_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def increase_twice_yield(a, arg):
	if is_num(a):
		yield a+2
	elif is_str(a):
		if len(a) == 1:
			yield chr(ord(a)+2)
		else:
			yield ''.join([b for n in a for b in increase_twice_yield(n, arg)])
	elif is_list(a):
		yield [b for n in a for b in increase_twice_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def decrease_twice_yield(a, arg):
	if is_num(a):
		yield a-2
	elif is_str(a):
		if len(a) == 1:
			yield chr(ord(a)-2)
		else:
			yield ''.join([b for n in a for b in decrease_twice_yield(n, arg)])
	elif is_list(a):
		yield [b for n in a for b in decrease_twice_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def ceiling_yield(a, arg):
	if is_num(a):
		yield math.ceil(a)
	elif is_list(a):
		yield [b for n in a for b in ceiling_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def is_square(n):
	s = round(n**.5)
	return int(n == s*s)

def is_square_yield(a, arg):
	yield is_square(a)

def get_sqrt_yield(a, arg):
	if is_num(a):
		yield math.sqrt(a)
	elif is_list(a):
		yield [math.sqrt(n) for n in a]
	elif is_str(a):
		yield a.split("\n")
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_cube_yield(a, arg):
	if is_num(a):
		yield a*a*a
	elif is_list(a):
		yield [n*n*n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_square_yield(a, arg):
	if is_num(a):
		yield a*a
	elif is_list(a):
		yield [n*n for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_self_product_or_collatz_yield(a, arg):
	if is_list(a):
		yield [list(n) for n in itertools.product(a, a)]
	elif is_int(a):
		if a % 2 == 0:
			yield a//2
		else:
			yield 3*a+1
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def is_prime(n):
	if n < 0:
		return 0
	if n < 10:
		return [0,0,1,1,0,1,0,1,0,0,0][n]
	for div in range(2, int(n**.5)+1):
		if n % div == 0:
			return 0
	return 1

def is_prime_yield(a, arg):
	if is_int(a):
		yield is_prime(a)
	elif is_list(a):
		yield [is_prime(n) for n in a]
	elif is_str(a):
		yield a.split()
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def gamma_yield(a, arg):
	if is_int(a):
		p = 1
		for i in range(1, a+1):
			p *= i
		yield p
	elif is_num(a):
		yield math.gamma(a+1)
	elif is_str(a):
		yield a.lower()
	elif is_list(a):
		yield [b for n in a for b in gamma_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def char_to_ord(a):
	res = 0
	for c in a[::-1]:
		res *= 256
		res += get_ord(c)
	return res

def ord_to_char(a):
	res = ""
	while a > 0:
		c = a % 256
		res += get_char(c)
		a //= 256
	return res

def ord_or_char_yield(a, arg):
	if is_str(a):
		yield char_to_ord(a)
	elif is_int(a):
		yield ord_to_char(a)
	elif is_list(a):
		yield [b for n in a for b in ord_or_char_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))


def decrease_yield(a, arg):
	if is_num(a):
		yield a-1
	elif is_str(a):
		if len(a) == 1:
			yield chr(ord(a)-1)
		else:
			yield ''.join([b for n in a for b in decrease_yield(n, arg)])
	elif is_list(a):
		yield [b for n in a for b in decrease_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def increase_yield(a, arg):
	if is_num(a):
		yield a+1
	elif is_str(a):
		if len(a) == 1:
			yield chr(ord(a)+1)
		else:
			yield ''.join([b for n in a for b in increase_yield(n, arg)])
	elif is_list(a):
		yield [b for n in a for b in increase_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def discard_tos_yield(a, arg):
	if False:
		yield 1

def wrap_in_array_yield(a, arg):
	yield [a]

def print_lines_yield(a, arg):
	if is_list(a):
		yield '\n'.join([str(n) for n in a])
	else:
		yield a
		yield "\n"

def print_without_popping_yield(a, arg):
	print(a)
	yield a

def print_with_newline_yield(a, arg):
	print(a)
	if False:
		yield 1

def print_without_newline_yield(a, arg):
	print(a, end = "")
	if False:
		yield 1

def is_truthy_filter_yield(a, arg):
	if is_list(a):
		if not is_falsey(a):
			yield [n for n in a if not is_falsey(n)]
	elif is_str(a):
		if not is_falsey(a):
			yield a
	elif is_num(a):
		if not is_falsey(a):
			yield a
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def length_with_pop_yield(a, arg):
	if is_int(a):
		yield len(str(a))
	elif is_str(a):
		yield len(a)
	elif is_list(a):
		yield len(a)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def to_base(a, b):
	res = []
	while a:
		res.append(a % b)
		a //= b
	return res

def from_base(l, b):
	res = 0
	for i, a in enumerate(l):
		res += a*b**i
	return res

def to_binary_yield(a, arg):
	yield to_base(a, 2)

def from_binary_yield(a, arg):
	yield from_base(a, 2)

def to_base_string(a, b):
	return ''.join([str(n) for n in to_base(a, b)][::-1]) or '0'

def from_base_string(a, b):
	return from_base([int(n) for n in a[::-1]], b)

def to_binary_string_yield(a, arg):
	if is_int(a):
		yield to_base_string(a, 2)
	elif is_list(a):
		yield [to_base_string(n, 2) for n in a]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def from_binary_string_yield(a, arg):
	if is_list(a):
		yield [from_base_string(n, 2) for n in a]
	elif is_str(a):
		yield from_base_string(a, 2)
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def duplicate(a, arg = None):
	for i in range(2):
		yield a

def triplicate(a, arg = None):
	for i in range(3):
		yield a

def quadruplicate(a, arg = None):
	for i in range(4):
		yield a

def join_list_without_separator_yield(a, arg):
	if is_list(a):
		if a == []:
			yield 0
		elif a and is_int(a[0]):
			yield int(''.join([str(n) for n in a]))
		elif a and is_str(a[0]):
			yield ''.join([str(n) for n in a])
		else:
			raise ValueError("[%s]%s is not supported" % (type(a[0]),arg.char))
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def convert_hexadecimal_yield(a, arg):
	if is_int(a):
		yield "%X" % a
	elif is_str(a):
		yield int(a, 16)
	elif is_list(a):
		yield [b for n in a for b in convert_hexadecimal_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_absolute_value_yield(a, arg):
	if is_num(a):
		yield abs(a)
	elif is_list(a):
		yield [b for n in a for b in get_absolute_value_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_average_of_list_yield(a, arg):
	if is_list(a):
		yield sum(a)/float(len(a))
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def get_diff_of_list_yield(a, arg):
	if is_list(a):
		diffs = []
		for i in range(len(a)-1):
			diffs.append(a[i+1]-a[i])
		yield diffs
	elif is_int(a):
		diffs = []
		for i in range(len(str(a))-1):
			diffs.append(int(str(a)[i+1])-int(str(a)[i]))
		yield diffs
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def invert_rational_yield(a, arg):
	if is_num(a):
		yield 1/a
	elif is_list(a):
		yield [b for n in a for b in invert_rational_yield(n, arg)]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
