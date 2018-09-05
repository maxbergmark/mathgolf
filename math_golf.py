import math
import sys
from collections import namedtuple
import datetime, time
import itertools

Argument = namedtuple("Argument", ["char", "code"])
DEBUG = False

code_page = "☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼S!\"#$%&'()*+,-./0123456789:;" \
+ "<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂Ç" \
+ "üéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞" \
+ "╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■ "

class StdIn():

	def __init__(self, lst):
		self.index = 0
		self.list = lst

	def pop(self):
		ret = self.list[self.index]
		self.index = (self.index+1) % len(self.list)
		return ret

def fibonnaci(n):
	a, b = 0, 1
	for i in range(n//2):
		a, b = a+b, a+2*b
	return [a, b][n%2]

def is_prime(n):
	if n < 0:
		return 0
	if n < 10:
		return [0,0,1,1,0,1,0,1,0,0,0][n]
	for div in range(2, int(n**.5)+1):
		if n % div == 0:
			return 0
	return 1

def is_str(n):
	return type(n) is str

def is_num(n):
	return type(n) is int or type(n) is float

def is_int(n):
	return is_num(n) and float(n).is_integer()

def is_list(n):
	return type(n) is list

def is_equal(a, b):
	yield int(a == b)
def is_less(a, b):
	yield int(a < b)
def is_greater(a, b):
	yield int(a > b)
def is_not(a, b):
	yield int(a != b)

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
	while stack and stack.pop():
		yield i
		i += 1

def while_false_pop(stack):
	i = 0
	while stack and not stack.pop():
		yield i
		i += 1

def for_looping(n):
	for i in range(n):
		yield i

def evaluate(code, stdin, stack = [], level = 0):
	# stack = []
	monads = {"¶": is_prime, "_": duplicate, "∙": triplicate, "·": quadruplicate}
	binary_monads = {"â": to_base, "ä": from_base}
	dinads = {"<": is_less, "=": is_equal, ">": is_greater, "¡": is_not}
	loop_handlers = {
		"↑": while_true_no_pop,
		"↓": while_false_no_pop,
		"→": while_true_pop,
		"←": while_false_pop
	}
	loop_types = set("↑↓→←*")
	block_creators = set("ÄÅÉæÆ{")
	loop_counter = 0

	while code:
		arg = code.pop()
		if 2 <= arg.code <= 10:
			stack.append(2**(arg.code+2))
		elif 11 <= arg.code <= 18:
			stack.append(10**(arg.code-10))
		elif arg.char == "¶":
			stack.append(is_prime(stack.pop()))
		elif arg.char == "§":
			a = stack.pop()
			b = stack.pop()
			if is_num(a) and is_list(b):
				stack.append(b[a % len(b)])
			elif is_list(a) and is_num(b):
				stack.append(a[b % len(a)])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "!":
			a = stack.pop()
			if is_num(a):
				if is_int(a):
					v = int(math.gamma(a+1))
				else:
					v = math.gamma(a+1)
			elif is_list(a):
				v = [int(math.gamma(n+1)) if is_int(n) else math.gamma(n+1) for n in a]
			stack.append(v)

		elif arg.char == "\"":
			s = ""
			c = "" if not code else code.pop().char
			while c != "\"" and code:
				if c == "\\":
					s += code.pop().char
				else:
					s += c
				c = code.pop().char
			stack.append(s)

		elif arg.char == "#":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_num(b):
				stack.append(a**b)
			elif is_num(a) and is_list(b):
				stack.append([a**n for n in b])
			elif is_list(a) and is_num(b):
				stack.append([n**b for n in a])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "%":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_num(b):
				stack.append(a%b)
			elif is_num(a) and is_list(b):
				stack.append([n for n in b[::n]])
			elif is_list(a) and is_num(b):
				stack.append([n%b for n in a])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "'":
			stack.append(code.pop().char)
		elif arg.char == "(":
			v = stack.pop()
			if type(v) is int or type(v) is float:
				stack.append(v-1)
			if type(v) is list:
				stack.append([n-1 for n in v])
		elif arg.char == ")":
			v = stack.pop()
			if type(v) is int or type(v) is float:
				stack.append(v+1)
			if type(v) is list:
				stack.append([n+1 for n in v])

		elif arg.char == "*":
			b = stack.pop()
			a = stack.pop()
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
			b = stack.pop()
			a = stack.pop()
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

		elif "0" <= arg.char <= "9":
			stack.append(int(arg.char))

		elif arg.char == ";":
			stack.pop()

		elif arg.char == "<":
			a, b = stack.pop(), stack.pop()
			stack.append(int(all(is_less(a, b))))
		elif arg.char == "=":
			a, b = stack.pop(), stack.pop()
			stack.append(int(all(is_equal(a, b))))
		elif arg.char == ">":
			a, b = stack.pop(), stack.pop()
			stack.append(int(all(is_greater(a, b))))

		elif arg.char == "?":
			stack.append(stack.pop(-3))
		elif arg.char == "@":
			stack.append(stack.pop(-3))
			stack.append(stack.pop(-3))

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
			ret = evaluate(code, stdin, [], level+1)
			stack.append(ret)
		elif arg.char == "\\":
			stack.append(stack.pop(-2))
		elif arg.char == "]":
			if level > 0:
				return stack
			else:
				stack = [stack]

		elif arg.char == "a":
			stack.append([stack.pop()])
		elif "b" <= arg.char <= "d":
			stack.append(ord("a") - ord(arg.char))
		elif arg.char == "e":
			stack.append(math.e)
		elif arg.char == "f":
			a = stack.pop()
			if is_int(a):
				stack.append(fibonnaci(a))
			elif is_list(a):
				stack.append([fibonnaci(n) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "g":
			op = code.pop().char
			a = stack.pop()
			if op in monads and is_list(a):
				stack.append([n for n in a if all(monads[op](n))])
			elif op in binary_monads and is_list(a):
				stack.append([n for n in a if all(binary_monads[op](n, 2))])
			elif op in dinads:
				b = stack.pop()
				if is_list(a) and is_num(b):
					stack.append([n for n in a if all(dinads[op](n, b))])
				elif is_num(a) and is_list(b):
					stack.append([n for n in b if all(dinads[op](a, n))])
				elif is_list(a) and is_list(b):
					if len(a) == len(b):
						stack.append([na for na, nb in zip(a, b) if all(dinads[op](na, nb))])
					else:
						raise ValueError("Both lists need to be of equal length for filtering")
			else:
				raise ValueError("[%s]%s%s is not supported" % (type(a),arg.char, op))

		elif arg.char == "h":
			a = stack.pop()
			if is_list(a):
				stack.append(a)
				stack.append(len(a))
			elif is_str(a):
				stack.append(a)
				stack.append(len(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "i":
			a = stack.pop()
			if is_list(a):
				stack.append([int(n) if is_num(n) else n for n in a])
			elif is_num(a):
				stack.append(int(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "j":
			v = float(stdin.pop())
			stack.append(v)
		elif arg.char == "k":
			v = float(stdin.pop())
			stack.append(int(v))
		elif arg.char == "l":
			v = stdin.pop()
			stack.append(v)

		elif arg.char == "m":
			op = code.pop().char
			a = stack.pop()
			if op in monads and is_list(a):
				stack.append([v for n in a for v in monads[op](n)])
			elif op in binary_monads and is_list(a):
				stack.append([n for n in a if binary_monads[op](n, 2)])
			elif op in dinads:
				b = stack.pop()
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
			a = stack.pop()
			if is_list(a):
				print('\n'.join([str(n) for n in a]))
			else:
				print()
				stack.append(a)
		elif arg.char == "o":
			print(stack[-1])
		elif arg.char == "p":
			print(stack.pop())
		elif arg.char == "q":
			print(stack.pop(), end='')
		elif arg.char == "r":
			stack.append(list(range(stack.pop())))
		elif arg.char == "s":
			a = stack.pop()
			if is_list(a):
				stack.append(sorted(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "t":
			now = datetime.datetime.now()
			stack.append(int(
				time.mktime(now.timetuple())*1e3 + now.microsecond//1e3
			))
		elif arg.char == "z":
			a = stack.pop()
			if is_list(a):
				stack.append(sorted(a, reverse = True))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "~":
			a = stack.pop()
			if is_num(a):
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
			a = stack.pop()
			if is_int(a):
				stack.append(to_base(a, 2))
			elif is_list(a):
				stack.append([to_base(n, 2) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ä":
			a = stack.pop()
			if is_list(a):
				if len(a) > 0 and is_list(a[0]):
					stack.append([from_base(n, 2) for n in a])
				else:
					stack.append(from_base(a, 2))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "à":
			a = stack.pop()
			if is_int(a):
				stack.append(to_base_string(a, 2))
			elif is_list(a):
				stack.append([to_base_string(n, 2) for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "å":
			a = stack.pop()
			if is_list(a):
				stack.append([from_base_string(n, 2) for n in a])
			elif is_str(a):
				stack.append(from_base_string(a, 2))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ç":
			a = stack.pop()
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

		elif arg.char == "ï":
			stack.append(loop_counter)


		elif arg.char in block_creators:
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
			elif arg.char == "{":
				c = []
				temp = [] if not code else code.pop()
				while temp.char != "}" and code:
					c.append(temp)
					temp = code.pop()
				c = c[::-1]
			loop_type = code.pop()

			if loop_type.char in loop_types:
				if loop_type.char == "*":
					limit = stack.pop()
					for i in for_looping(limit):
						loop_counter = i
						stack = evaluate(c[:], stdin, stack, level+1)
				else:
					# stack.append(0)
					for i in loop_handlers[loop_type.char](stack):
						loop_counter = i
						stack = evaluate(c[:], stdin, stack, level+1)

		elif arg.char == "¥":
			a = stack.pop()
			if is_num(a):
				stack.append(a % 2)
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "ª":
			stack.append([1])
		elif arg.char == "º":
			stack.append([0])
		elif arg.char == "⌐":
			stack.append(stack.pop(0))
		elif arg.char == "¬":
			stack = [stack.pop()] + stack

		elif arg.char == "½":
			a = stack.pop()
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
			a = stack.pop()
			if is_num(a):
				if is_int(a):
					stack.append(a//4)
				else:
					stack.append(a/4)
			elif is_list(a):
				stack.append([n//4 if is_int(n) else n/4 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "¡":
			a = stack.pop()
			b = stack.pop()
			stack.append(is_not(a, b))

		elif arg.char == "«":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_num(b):
				stack.append(a<<b)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
		elif arg.char == "»":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_num(b):
				stack.append(a>>b)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "╤":
			a = stack.pop()
			if is_num(a):
				stack.append(list(range(-int(a), int(a)+1)))
		elif arg.char == "╒":
			a = stack.pop()
			if is_num(a):
				stack.append(list(range(1, int(a)+1)))


		elif arg.char == "▌":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_list(b):
				stack.append([a] + b)
			elif is_list(a) and is_num(b):
				stack.append([b] + a)
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
		elif arg.char == "▐":
			b = stack.pop()
			a = stack.pop()
			if is_num(a) and is_list(b):
				stack.append(b + [a])
			elif is_list(a) and is_num(b):
				stack.append(a + [b])
			else:
				raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

		elif arg.char == "α":
			b = stack.pop()
			a = stack.pop()
			stack.append([a, b])


		elif arg.char == "π":
			stack.append(math.pi)
		elif arg.char == "τ":
			stack.append(2*math.pi)
		elif arg.char == "Σ":
			a = stack.pop()
			if is_list(a):
				stack.append(sum(a))
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "φ":
			stack.append((1+math.sqrt(5))/2)
		elif arg.char == "⌠":
			a = stack.pop()
			if is_num(a):
				stack.append(a+2)
			elif is_list(a):
				stack.append([n+2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))
		elif arg.char == "⌡":
			a = stack.pop()
			if is_num(a):
				stack.append(a-2)
			elif is_list(a):
				stack.append([n-2 for n in a])
			else:
				raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

		elif arg.char == "_":
			a = stack.pop()
			for n in duplicate(a):
				stack.append(n)
		elif arg.char == "∙":
			a = stack.pop()
			for n in triplicate(a):
				stack.append(n)
		elif arg.char == "·":
			a = stack.pop()
			for n in quadruplicate(a):
				stack.append(n)

		elif arg.char == "√":
			a = stack.pop()
			if is_num(a):
				stack.append(math.sqrt(a))
			elif is_list(a):
				stack.append([math.sqrt(n) for n in a])

		elif arg.char == "ⁿ":
			a = stack.pop()
			if is_num(a):
				stack.append(a*a*a)
			elif is_list(a):
				stack.append([n*n*n for n in a])
		elif arg.char == "²":
			a = stack.pop()
			if is_num(a):
				stack.append(a*a)
			elif is_list(a):
				stack.append([n*n for n in a])
		elif arg.char == "■":
			a = stack.pop()
			if is_list(a):
				stack.append([list(n) for n in itertools.product(a, a)])


		else:
			raise ValueError("Not yet implemented: " + arg.char)
		if DEBUG:
			print(stack, arg)
			time.sleep(0.1)

	return stack

def print_list(l):
	return ''.join([str(s) if is_list(s) else str(s) for s in l])

if __name__ == '__main__':
	## doctest.testmod() ## <- Uncomment to run tests.
	if len(sys.argv) <= 1:
		print >> sys.stderr, 'usage: python %s [-d] <code file>' % sys.argv[0]
		sys.exit(1)

	if sys.argv[1] == '-d':
		DEBUG = True
		sys.argv.pop(1)

	code = open(sys.argv[1], 'r').read()
	commands = [code_page.index(c)+1 for c in code]
	code_list = [Argument(char, c) for char, c in zip(code, commands)][::-1]
	stdin = StdIn(list('' if sys.stdin.isatty() else sys.stdin.read().split()))
	result = evaluate(code_list, stdin)
	print(print_list(result))

