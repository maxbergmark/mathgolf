import math
import sys
from collections import namedtuple
import datetime, time
import itertools
import random
import resources.dictionary
from traceback import print_exc
from functools import reduce

Argument = namedtuple("Argument", ["char", "code"])
DEBUG = False

code_page = "☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !\"#$%&'()*+,-./0123456789:;" \
+ "<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂Ç" \
+ "üéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞" \
+ "╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■ "

class StdIn():

	def __init__(self, lst):
		self.index = 0
		self.list = lst

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == len(self.list):
			raise StopIteration
		self.index += 1
		return self.list[self.index-1]

	def pop(self):
		if self.list:
			ret = self.list[self.index]
			self.index = (self.index+1) % len(self.list)
			return ret
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
			raise StopIteration
		self.index += 1
		return self.list[self.index-1]

	def append(self, item):
		self.list.append(item)

	def pop(self, operator, index = -1):
		if self.list:
			return self.list.pop(index)
		raise IndexError("%s could not pop from stack" % operator)

def fibonnaci(n):
	a, b = 0, 1
	for i in range(n//2):
		a, b = a+b, a+2*b
	return [a, b][n%2]

def is_square(n):
	s = round(n**.5)
	return int(n == s*s)

def is_prime(n):
	if n < 0:
		return 0
	if n < 10:
		return [0,0,1,1,0,1,0,1,0,0,0][n]
	for div in range(2, int(n**.5)+1):
		if n % div == 0:
			return 0
	return 1

def gamma(n):
	if is_int(n):
		return int(math.gamma(n+1))
	elif is_num(n):
		return math.gamma(n+1)
	else:
		raise ValueError("unsupported type for gamma: %s" % type(n))

def gamma_yield(n):
	if is_int(n):
		yield int(math.gamma(n+1))
	elif is_num(n):
		yield math.gamma(n+1)
	else:
		raise ValueError("unsupported type for gamma: %s" % type(n))

def is_str(n):
	return type(n) is str

def is_num(n):
	return type(n) is int or type(n) is float

def is_int(n):
	return type(n) is int or is_num(n) and float(n).is_integer()

def is_list(n):
	return type(n) is list

def is_equal(a, b):
	yield int(a == b)

def is_less(a, b):
	yield int(a < b)

def is_greater(a, b):
	yield int(a > b)

def is_leq(a, b):
	yield int(a <= b)

def is_geq(a, b):
	yield int(a >= b)

def is_not(a, b):
	yield int(a != b)

def add_yield(a, b):
	yield a+b

def mult_yield(a, b):
	yield a*b

def add(a, b):
	return a+b

def mult(a, b):
	return a*b

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

def to_base_string(a, b):
	return ''.join([str(n) for n in to_base(a, b)]) or '0'

def from_base_string(a, b):
	return from_base([int(n) for n in a], b)

def duplicate(a):
	for i in range(2):
		yield a

def triplicate(a):
	for i in range(3):
		yield a

def quadruplicate(a):
	for i in range(4):
		yield a

def is_truthy(a):
	if is_num(a):
		return a != 0
	elif is_str(a):
		return len(a) > 0
	elif is_list(a):
		return any(map(is_truthy, a))

def is_falsey(a):
	if is_num(a):
		return a == 0
	elif is_str(a):
		return a == ""
	elif is_list(a):
		return not any(is_truthy(n) for n in a)

def while_true_no_pop(stack):
	i = 0
	while stack and stack[-1]:
		yield i
		i += 1

def while_false_no_pop(stack):
	i = 0
	while stack and not stack[-1]:
		yield i
		i += 1

def while_true_pop(stack):
	i = 0
	while stack and stack.pop("→"):
		yield i
		i += 1

def while_false_pop(stack):
	i = 0
	while stack and not stack.pop("←"):
		yield i
		i += 1

def do_while_true_no_pop(stack):
	i = 0
	while True:
		yield i
		i += 1
		if not (stack and stack[-1]):
			break

def do_while_false_no_pop(stack):
	i = 0
	while True:
		yield i
		i += 1
		if not (stack and not stack[-1]):
			break

def do_while_true_pop(stack):
	i = 0
	while True:
		yield i
		i += 1
		if not (stack and stack.pop("▲")):
			break

def do_while_false_pop(stack):
	i = 0
	while True:
		yield i
		i += 1
		if not (stack and not stack.pop("▼")):
			break

def decompress(string, compressed):
	decompressed = ""
	for i in range(len(string)):
		letter_idx = code_page.index(string[i])+1
		string_idx = (letter_idx >> 4) & 0xf
		decompressed += compressed[string_idx]
		string_idx = (letter_idx >> 0) & 0xf
		decompressed += compressed[string_idx]
	return decompressed

def create_block(arg, code):
	if arg.char == "Ä":
		c = code[-1:]
		code = code[:-1]
	elif arg.char == "Å":
		c = code[-2:]
		code = code[:-2]
	elif arg.char == "É":
		c = code[-3:]
		code = code[:-3]
	elif arg.char == "æ":
		c = code[-4:]
		code = code[:-4]
	elif arg.char == "Æ":
		c = code[-5:]
		code = code[:-5]
	elif arg.char == "ô":
		c = code[-6:]
		code = code[:-6]
	elif arg.char == "ö":
		c = code[-7:]
		code = code[:-7]
	elif arg.char == "ò":
		c = code[-8:]
		code = code[:-8]
	elif arg.char == "{":
		c = []
		temp = [] if not code else code.pop()
		while temp.char != "}" and code:
			c.append(temp)
			temp = code.pop()
		c = c[::-1]
	return c, code

def for_looping(n):
	for i in range(n):
		yield i

def evaluate(code, stdin, stack = Stack([]), level = 0, loop_counter = 0, loop_limit = 0, loop_value = None):

	monads = {
		"¶": is_prime,
		"!": gamma_yield,
		"_": duplicate,
		"∙": triplicate,
		"·": quadruplicate
	}
	binary_monads = {"â": to_base, "ä": from_base}
	dinads = {"<": is_less, "=": is_equal, ">": is_greater, "¡": is_not, "+": add_yield, "*": mult_yield, "≥": is_geq, "≤": is_leq}
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
	reducers = {"*": mult, "#": pow, "+": add}

	loop_types = set("↑↓→←∟↔▲▼*")
	block_creators = set("ÄÅÉæÆ{ôöò")
	string_creators = set("ûùÿ╢╖╕╣║╗")
	string_terminators = set("\"«»")
	compressed_letters_0 = "etaoinsrdluczbfp"
	compressed_letters_1 = "gwymvkxjqh ?*#.,"

	words = resources.dictionary.words

	while code:
		arg = code.pop()
		if 2 <= arg.code <= 10:
			stack.append(2**(arg.code+2))
		elif 11 <= arg.code <= 18:
			stack.append(10**(arg.code-10))
		elif arg.char == "¶":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(is_prime(a))
			elif is_list(a):
				stack.append([is_prime(n) for n in a])
			elif is_str(a):
				stack.append(a.split())
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "§":
			a = stack.pop(arg.char)
			b = stack.pop(arg.char)
			if is_int(a) and is_list(b):
				stack.append(b[a % len(b)])
			elif is_list(a) and is_int(b):
				stack.append(a[b % len(a)])
			elif is_int(a) and is_str(b):
				stack.append(b[a % len(b)])
			elif is_str(a) and is_int(b):
				stack.append(a[b % len(a)])
			elif is_list(a) and is_list(b):
				stack.append([a[n % len(a)] for n in b])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "!":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(gamma(a))
			elif is_list(a):
				stack.append([gamma(n) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "\"":
			s = ""
			c = "" if not code else code.pop().char
			while c not in  string_terminators and code:
				if c == "\\":
					s += code.pop().char
				else:
					s += c
				c = code.pop().char
			if c == "\"" or not code:
				if not code:
					s += c
				stack.append(s)
			else:
				if c == "«":
					compressed = "etaoinsrhluczbfp"
				elif c == "":
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

		elif arg.char == "#":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(a**b)
			elif is_num(a) and is_list(b):
				stack.append([a**n for n in b])
			elif is_list(a) and is_num(b):
				stack.append([n**b for n in a])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "%":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(a%b)
			elif is_num(a) and is_list(b):
				stack.append([n for n in b[::n]])
			elif is_list(a) and is_num(b):
				stack.append([n%b for n in a])
			elif is_num(a) and is_str(b):
				stack.append(''.join([n for n in b[::n]]))
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "'":
			stack.append(code.pop().char)

		elif arg.char == "(":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a-1)
			elif is_list(a):
				stack.append([n-1 for n in a])
			elif is_str(a):
				stack.append(''.join([chr(ord(n)-1) for n in a]))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == ")":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a+1)
			elif is_list(a):
				stack.append([n+1 for n in a])
			elif is_str(a):
				stack.append(''.join([chr(ord(n)+1) for n in a]))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "*":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(a*b)
			elif is_str(a) and is_num(b):
				stack.append(a*int(b))
			elif is_num(a) and is_str(b):
				stack.append(int(a)*b)
			elif is_num(a) and is_list(b):
				stack.append(a*b)
			elif is_list(a) and is_num(b):
				stack.append([n*b for n in a])
			elif is_list(a) and is_str(b):
				stack.append([n*b for n in a])
			elif is_list(a) and is_list(b):
				stack.append([list(n) for n in itertools.product(a, b)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "+":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(a+b)
			elif is_num(a) and is_list(b):
				stack.append([n+a for n in b])
			elif is_list(a) and is_num(b):
				stack.append([n+b for n in a])
			elif is_list(a) and is_list(b):
				stack.append(a+b)
			elif is_str(a) and is_num(b):
				stack.append(a+str(b))
			elif is_num(a) and is_str(b):
				stack.append(str(a)+b)
			elif is_str(a) and is_list(b):
				stack.append([a+str(n) for n in b])
			elif is_list(a) and is_str(b):
				stack.append([str(n)+b for n in a])
			elif is_str(a) and is_str(b):
				stack.append(a+b)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "-":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(a-b)
			elif is_num(a) and is_list(b):
				stack.append([a-n for n in b])
			elif is_list(a) and is_num(b):
				stack.append([n-b for n in a])
			elif is_list(a) and is_list(b):
				stack.append([n for n in a if n not in set(b)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "/":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_int(a) and is_int(b):
				stack.append(a//b)
			elif is_num(a) and is_num(b):
				stack.append(a/b)
			elif is_num(a) and is_list(b):
				stack.append([a/n for n in b])
			elif is_list(a) and is_num(b):
				stack.append([n/b for n in a])
			elif is_list(a) and is_list(b):
				stack.append([n2 for n2 in b if n2 not in set([n for n in a if n not in set(b)])])
			elif is_str(a) and is_int(b):
				stack.append([a[i*b:(i+1)*b] for i in range(math.ceil(len(a)/b))])

			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif "0" <= arg.char <= "9":
			stack.append(int(arg.char))

		elif arg.char == ";":
			stack.pop(arg.char)

		elif arg.char == "<":
			a, b = stack.pop(arg.char), stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(int(all(is_less(a, b))))
			elif is_int(a) and is_list(b):
				stack.append([b[i%len(b)] for i in range(a)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "=":
			a, b = stack.pop(arg.char), stack.pop(arg.char)
			stack.append(int(all(is_equal(a, b))))
		elif arg.char == ">":
			a, b = stack.pop(arg.char), stack.pop(arg.char)
			stack.append(int(all(is_greater(a, b))))

		elif arg.char == "?":
			if len(stack) < 3:
				raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			stack.append(stack.pop(arg.char, -3))
		elif arg.char == "@":
			if len(stack) < 3:
				raise IndexError("%s requires at least 3 elements on the stack" % arg.char)
			stack.append(stack.pop(arg.char, -3))
			stack.append(stack.pop(arg.char, -3))

		elif "A" <= arg.char <= "E":
			val = 11 + ord(arg.char) - ord("A")
			stack.append(val)
		elif "F" <= arg.char <= "T":
			val = 17 + ord(arg.char) - ord("F")
			stack.append(val)
		elif "U" <= arg.char <= "Z":
			val = 33 + ord(arg.char) - ord("U")
			stack.append(val)

		elif arg.char == "[":
			ret = evaluate(code, stdin, Stack([]), level+1)
			stack.append(ret.list)
		elif arg.char == "\\":
			stack.append(stack.pop(arg.char, -2))
		elif arg.char == "]":
			if level > 0:
				return stack
			else:
				stack = Stack([stack.list])

		elif arg.char == "a":
			stack.append([stack.pop(arg.char)])

		elif "b" <= arg.char <= "d":
			stack.append(ord("a") - ord(arg.char))

		elif arg.char == "e":
			stack.append(math.e)

		elif arg.char == "f":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(fibonnaci(a))
			elif is_list(a):
				stack.append([fibonnaci(n) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "g":
			op = code.pop()
			a = stack.pop(arg.char)
			if op.char in monads and is_list(a):
				stack.append([n for n in a if all(monads[op.char](n))])
			elif op.char in binary_monads and is_list(a):
				stack.append([n for n in a if all(binary_monads[op.char](n, 2))])
			elif op.char in dinads:
				b = stack.pop(arg.char)
				if is_list(a) and is_num(b):
					stack.append([n for n in a if all(dinads[op.char](n, b))])
				elif is_num(a) and is_list(b):
					stack.append([n for n in b if all(dinads[op.char](a, n))])
				elif is_list(a) and is_list(b):
					if len(a) == len(b):
						stack.append([na for na, nb in zip(a, b) if all(dinads[op.char](na, nb))])
					else:
						raise ValueError("Both lists need to be of equal length for filtering")
			elif op.char in block_creators and is_list(a):
				c, code = create_block(op, code)
				stack.append([n for n in a if evaluate(c[:], stdin, Stack([n]), level+1)[0]])
			else:
				raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op))

		elif arg.char == "h":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append(a)
				stack.append(len(a))
			elif is_str(a):
				stack.append(a)
				stack.append(len(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "i":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append([int(n) if is_num(n) else n for n in a])
			elif is_num(a):
				stack.append(int(a))
			elif is_str(a):
				stack.append(int(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "j":
			v = float(stdin.pop())
			stack.append(v)
		elif arg.char == "k":
			v = int(stdin.pop())
			stack.append(v)
		elif arg.char == "l":
			v = stdin.pop()
			stack.append(v)

		elif arg.char == "m":
			op = code.pop().char
			a = stack.pop(arg.char)
			if op in monads and is_list(a):
				stack.append([v for n in a for v in monads[op](n)])
			elif op in binary_monads and is_list(a):
				stack.append([n for n in a if binary_monads[op](n, 2)])
			elif op in dinads:
				b = stack.pop(arg.char)
				if is_list(a) and is_num(b):
					stack.append([v for n in a for v in dinads[op](n, b)])
				elif is_num(a) and is_list(b):
					stack.append([v for n in b for v in dinads[op](a, n)])
				elif is_list(a) and is_list(b):
					if len(a) == len(b):
						stack.append([v for na, nb in zip(a, b) for v in dinads[op](na, nb)])
					else:
						raise ValueError("Both lists need to be of equal length for filtering")
			else:
				raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op))


		elif arg.char == "n":
			a = stack.pop(arg.char)
			if is_list(a):
				print('\n'.join([str(n) for n in a]))
			else:
				print()
				stack.append(a)
		elif arg.char == "o":
			print(stack[-1])
		elif arg.char == "p":
			print(stack.pop(arg.char))
		elif arg.char == "q":
			print(stack.pop(arg.char), end='')
		elif arg.char == "r":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(list(range(a)))
			elif is_list(a):
				stack.append([list(range(n)) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "s":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append(sorted(a))
			elif is_str(a):
				stack.append(''.join(sorted(a)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "t":
			now = datetime.datetime.now()
			stack.append(int(
				time.mktime(now.timetuple())*1e3 + now.microsecond//1e3
			))

		elif arg.char == "u":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_list(a) and is_str(b):
				stack.append(b.join([str(n) for n in a]))
			elif is_str(a) and is_list(b):
				stack.append(a.join([str(n) for n in b]))
			elif(is_str(a) and is_str(b)):
				stack.append(b.join(list(a)))
			elif is_list(a) and is_list(b):
				stack.append([n.join(a) for n in b])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "v":
			stack.append(random.randint(-2**31, 2**31-1))

		elif arg.char == "w":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(random.randint(0, a))
			elif is_list(a):
				stack.append(random.choice(a))
			elif is_str(a):
				stack.append(random.choice(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "x":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(str(a)[::-1]))
			elif is_list(a):
				stack.append(a[::-1])
			elif is_str(a):
				stack.append(a[::-1])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))


		elif arg.char == "z":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append(sorted(a, reverse = True))
			elif is_str(a):
				stack.append(''.join(sorted(a, reverse = True)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "⌂":
			stack.append("*")
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

		elif arg.char == "â":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(to_base(a, 2))
			elif is_list(a):
				stack.append([to_base(n, 2) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ä":
			a = stack.pop(arg.char)
			if is_list(a):
				if len(a) > 0 and is_list(a[0]):
					stack.append([from_base(n, 2) for n in a])
				else:
					stack.append(from_base(a, 2))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "à":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(to_base_string(a, 2))
			elif is_list(a):
				stack.append([to_base_string(n, 2) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "å":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append([from_base_string(n, 2) for n in a])
			elif is_str(a):
				stack.append(from_base_string(a, 2))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ç":
			a = stack.pop(arg.char)
			if is_list(a):
				if not is_falsey(a):
					stack.append([n for n in a if not is_falsey(n)])
			elif is_str(a):
				if not is_falsey(a):
					stack.append(a)
			elif is_num(a):
				if not is_falsey(a):
					stack.append(a)
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

		elif arg.char == "£":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(len(a))
			elif is_list(a):
				stack.append(len(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "¥":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a % 2)
			elif is_list(a):
				stack.append([n % 2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ó":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(2**a)
			elif is_list(a):
				stack.append([2**n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "ú":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(10**a))
			elif is_num(a):
				stack.append(10**a)
			elif is_list(a):
				stack.append([10**n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ñ":
			a = stack.pop(arg.char)
			if is_int(a):
				a = str(a)
				stack.append(int(a+a[::-1][1:]))
			elif is_list(a):
				stack.append(a+a[::-1][1:])
			elif is_str(a):
				stack.append(a+a[::-1][1:])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ª":
			stack.append([1])
		elif arg.char == "º":
			stack.append([0])

		elif arg.char == "¿":
			a = stack.pop(arg.char)
			if is_truthy(a):
				code.pop(1)
			else:
				code.pop()

		elif arg.char == "⌐":
			stack.append(stack.pop(arg.char, 0))
		elif arg.char == "¬":
			stack = Stack([stack.pop(arg.char)] + stack.list())

		elif arg.char == "½":
			a = stack.pop(arg.char)
			if is_num(a):
				if is_int(a):
					stack.append(a//2)
				else:
					stack.append(a/2)
			elif is_list(a):
				stack.append([n//2 if is_int(n) else n/2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "¼":
			a = stack.pop(arg.char)
			if is_num(a):
				if is_int(a):
					stack.append(a//4)
				else:
					stack.append(a/4)
			elif is_list(a):
				stack.append([n//4 if is_int(n) else n/4 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "░":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(str(a))
			elif is_list(a):
				stack.append([str(n) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "▒":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append([int(n) for n in str(a)])
			elif is_str(a):
				stack.append(list(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))


		elif arg.char == "¡":
			a = stack.pop(arg.char)
			b = stack.pop(arg.char)
			stack.append(int(all(is_not(a, b))))

		elif arg.char == "┤":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a[:-1])
				stack.append(a[-1])
			elif is_list(a):
				stack.append(a[:-1])
				stack.append(a[-1])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╡":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a[:-1])
			elif is_list(a):
				stack.append(a[:-1])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "┐":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a)
				stack.append(a-1)
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "└":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a)
				stack.append(a+1)
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "┴":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(int(a == 1))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "┬":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(int(a == 0))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))


		elif arg.char == "├":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a[1:])
				stack.append(a[0])
			elif is_list(a):
				stack.append(a[1:])
				stack.append(a[0])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╞":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a[1:])
			elif is_list(a):
				stack.append(a[1:])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "─":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append([n for n in range(1, a+1) if a%n == 0])
			elif is_list(a):
				stack.append([n for l in a for n in l])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╟":
			stack.append(60)
		elif arg.char == "╚":
			stack.append(3600)
		elif arg.char == "╔":
			stack.append(86400)

		elif arg.char == "╩":
			next_char = code.pop().code
			stack.append(words[next_char])

		elif arg.char == "╦":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(words[a])
			elif is_list(a):
				stack.append([words[n] if is_int(n) else n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╨":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(2**int(math.log(a, 2)+1))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╥":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(2**int(math.log(a, 2)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╤":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(list(range(-int(a), int(a)+1)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "╒":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(list(range(1, int(a)+1)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "▌":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_list(b):
				stack.append([a] + b)
			elif is_list(a) and is_num(b):
				stack.append([b] + a)
			elif is_str(a) and is_list(b):
				stack.append([a] + b)
			elif is_list(a) and is_str(b):
				stack.append([b] + a)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "▐":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_num(a) and is_list(b):
				stack.append(b + [a])
			elif is_list(a) and is_num(b):
				stack.append(a + [b])
			elif is_str(a) and is_list(b):
				stack.append(b + [a])
			elif is_list(a) and is_str(b):
				stack.append(a + [b])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

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

		elif arg.char == "π":
			stack.append(math.pi)
		elif arg.char == "τ":
			stack.append(2*math.pi)

		elif arg.char == "╫":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(bin(a)[3:]+'1', 2))
			elif is_list(a):
				stack.append(a[1:] + [a[0]])
			elif is_str(a):
				stack.append(a[1:] + a[0])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "╪":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(str(a&1)+bin(a)[2:-1], 2))
			elif is_list(a):
				stack.append([a[-1]] + a[:-1])
			elif is_str(a):
				stack.append(a[-1] + a[:-1])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "┘":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(is_truthy(a)))
			elif is_list(a):
				stack.append([int(is_truthy(n)) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "┌":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(int(is_falsey(a)))
			elif is_list(a):
				stack.append([int(is_falsey(n)) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "▀":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(''.join(list(set(a))))
			elif is_list(a):
				stack.append(list(set(a)))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "Σ":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(sum(int(d) for d in str(a)))
			elif is_list(a):
				if len(a) > 0 and is_int(a[0]):
					stack.append(sum(a))
				elif len(a) > 0 and is_str(a[0]):
					stack.append(''.join(a))
				else:
					stack.append(0)
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "σ":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a.lstrip("0"))
			elif is_list(a):
				if len(a) > 0 and is_int(a[0]):
					stack.append(["" if n == 0 else str(n) for n in a])
				elif len(a) > 0 and is_str(a[0]):
					stack.append([n.lstrip("0") for n in a])
				else:
					stack.append([])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "Φ":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_int(a) and is_list(b):
				b[a % len(b)] += 1
				stack.append(b)
			elif is_list(a) and is_int(b):
				a[b % len(a)] += 1
				stack.append(a)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "Θ":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_int(a) and is_list(b):
				b[a % len(b)] -= 1
				stack.append(b)
			elif is_list(a) and is_int(b):
				a[b % len(a)] -= 1
				stack.append(a)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

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

		elif arg.char == "δ":
			a = stack.pop(arg.char)
			if is_str(a):
				stack.append(a.capitalize())
			elif is_list(a):
				stack.append([n.capitalize() if is_str(n) else n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ε":
			a = stack.pop(arg.char)
			if is_list(a):
				operator = code.pop().char
				if operator in reducers:
					stack.append(reduce(reducers[operator], a))
				else:
					raise ValueError("[%s]%s%s is not a valid reduction" % (a, arg.char, operator))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))


		elif arg.char == "∞":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a*2)
			elif is_list(a):
				stack.append([n*2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "φ":
			stack.append((1+math.sqrt(5))/2)

		elif arg.char == "≥":
			a, b = stack.pop(arg.char), stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(int(all(is_geq(a, b))))
			elif is_int(a) and is_list(b):
				stack.append([b[i%len(b)] for i in range(a)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "≤":
			a, b = stack.pop(arg.char), stack.pop(arg.char)
			if is_num(a) and is_num(b):
				stack.append(int(all(is_leq(a, b))))
			elif is_int(a) and is_list(b):
				stack.append([b[i%len(b)] for i in range(a)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))



		elif arg.char == "⌠":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a+2)
			elif is_list(a):
				stack.append([n+2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "⌡":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a-2)
			elif is_list(a):
				stack.append([n-2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "÷":
			b = stack.pop(arg.char)
			a = stack.pop(arg.char)
			if is_int(a) and is_int(b):
				stack.append(int(a%b == 0))
			elif is_int(a) and is_list(b):
				stack.append([int(a%n == 0) for n in b])
			elif is_list(a) and is_int(b):
				stack.append([int(n%b == 0) for n in a])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))


		elif arg.char == "_":
			a = stack.pop(arg.char)
			for n in duplicate(a):
				stack.append(n)
		elif arg.char == "`":
			stack.append(stack[-2])
			stack.append(stack[-2])
		elif arg.char == "°":
			a = stack.pop(arg.char)
			if is_int(a):
				stack.append(is_square(a))
		elif arg.char == "∙":
			a = stack.pop(arg.char)
			for n in triplicate(a):
				stack.append(n)
		elif arg.char == "·":
			a = stack.pop(arg.char)
			for n in quadruplicate(a):
				stack.append(n)

		elif arg.char == "√":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(math.sqrt(a))
			elif is_list(a):
				stack.append([math.sqrt(n) for n in a])
			elif is_str(a):
				stack.append(list(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ⁿ":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a*a*a)
			elif is_list(a):
				stack.append([n*n*n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "²":
			a = stack.pop(arg.char)
			if is_num(a):
				stack.append(a*a)
			elif is_list(a):
				stack.append([n*n for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "■":
			a = stack.pop(arg.char)
			if is_list(a):
				stack.append([list(n) for n in itertools.product(a, a)])
			if is_int(a):
				if a % 2 == 0:
					stack.append(a//2)
				else:
					stack.append(3*a+1)
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == " ":
			stack.append(" ")
		elif arg.char == " ":
			stack = Stack([stack.pop(arg.char)])

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
	## doctest.testmod() ## <- Uncomment to run tests.
	if len(sys.argv) <= 1:
		print('usage: python %s [-d] <code file>' % sys.argv[0])
		sys.exit(1)

	if sys.argv[1] == '-d':
		DEBUG = True
		sys.argv.pop(1)

	code_bytes = open(sys.argv[1], 'rb').read()
	code = parse_input(code_bytes)
	commands = [code_page.index(c)+1 for c in code]
	code_list = [Argument(char, c) for char, c in zip(code, commands)][::-1]
	stdin = StdIn(list('' if sys.stdin.isatty() else sys.stdin.read().split()))
	try:
		result = evaluate(code_list, stdin)
		print(print_list(result))
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print()
		print_exc()
		print("%s (line %d): %s" % (type(e).__name__, exc_tb.tb_lineno, e))
