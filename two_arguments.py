from check_type import *
import math

def get_list_or_string_item(a, b, arg):
	if is_int(a) and is_list(b):
		yield b[a % len(b)]
	elif is_list(a) and is_int(b):
		yield a[b % len(a)]
	elif is_int(a) and is_str(b):
		yield b[a % len(b)]
	elif is_str(a) and is_int(b):
		yield a[b % len(a)]
	elif is_list(a) and is_list(b):
		yield [a[n % len(a)] for n in b]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))


def is_equal(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a == b)
	elif type(a) == type(b):
		yield int(a == b)
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_less(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a < b)
	elif is_int(a) and is_list(b):
		yield [b[i%len(b)] for i in range(a)]
	elif is_list(a) and is_int(b):
		yield [a[i%len(a)] for i in range(b)]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_greater(a, b, arg):
	if type(a) == type(b):
		yield int(a > b)
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_leq(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a <= b)
	elif is_int(a) and is_list(b):
		yield [b[i%len(b)] for i in range(a)]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_geq(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a >= b)
	elif is_int(a) and is_list(b):
		yield [b[i%len(b)] for i in range(a)]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_not(a, b, arg):
	if type(a) == type(b):
		yield int(a != b)
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def add_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a+b
	elif is_num(a) and is_list(b):
		yield [n+a for n in b]
	elif is_list(a) and is_num(b):
		yield [n+b for n in a]
	elif is_list(a) and is_list(b):
		yield a+b
	elif is_str(a) and is_num(b):
		yield a+str(b)
	elif is_num(a) and is_str(b):
		yield str(a)+b
	elif is_str(a) and is_list(b):
		yield [a+str(n) for n in b]
	elif is_list(a) and is_str(b):
		yield [str(n)+b for n in a]
	elif is_str(a) and is_str(b):
		yield a+b
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def subtract_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a-b
	elif is_num(a) and is_list(b):
		yield [a-n for n in b]
	elif is_list(a) and is_num(b):
		yield [n-b for n in a]
	elif is_list(a) and is_list(b):
		yield [n for n in a if n not in set(b)]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def mult_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a*b
	elif is_str(a) and is_num(b):
		yield a*int(b)
	elif is_num(a) and is_str(b):
		yield int(a)*b
	elif is_num(a) and is_list(b):
		yield a*b
	elif is_list(a) and is_num(b):
		yield [n*b for n in a]
	elif is_list(a) and is_str(b):
		yield [n*b for n in a]
	elif is_list(a) and is_list(b):
		yield [list(n) for n in itertools.product(a, b)]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def divide_yield(a, b, arg):
	if is_int(a) and is_int(b):
		yield a//b
	elif is_num(a) and is_num(b):
		yield a/b
	elif is_num(a) and is_list(b):
		yield [a//n if is_int(a) else a/n for n in b]
	elif is_list(a) and is_num(b):
		yield [n//b if is_int(b) else n/b for n in a]
	elif is_list(a) and is_list(b):
		yield [n2 for n2 in b if n2 not in set([n for n in a if n not in set(b)])]
	elif is_str(a) and is_int(b):
		yield [a[i*b:(i+1)*b] for i in range(math.ceil(len(a)/b))]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def power_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a**b
	elif is_num(a) and is_list(b):
		yield [a**n for n in b]
	elif is_list(a) and is_num(b):
		yield [n**b for n in a]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def modulo_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a%b
	elif is_int(a) and is_list(b):
		yield [n for n in b[::a]]
	elif is_list(a) and is_num(b):
		yield [n%b for n in a]
	elif is_num(a) and is_str(b):
		yield ''.join([n for n in b[::n]])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def join_yield(a, b, arg):
	if is_list(a) and is_str(b):
		yield b.join([str(n) for n in a])
	elif is_str(a) and is_list(b):
		yield a.join([str(n) for n in b])
	elif(is_str(a) and is_str(b)):
		yield b.join(list(a))
	elif is_list(a) and is_list(b):
		yield [n.join(a) for n in b]
	else:
		raise ValueError("[%s]%s is not supported" % (type(a),arg.char))

def prepend_list_or_string_yield(a, b, arg):
	if is_num(a) and is_list(b):
		yield [a] + b
	elif is_list(a) and is_num(b):
		yield [b] + a
	elif is_str(a) and is_list(b):
		yield [a] + b
	elif is_list(a) and is_str(b):
		yield [b] + a
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def append_list_or_string_yield(a, b, arg):
	if is_num(a) and is_list(b):
		yield b + [a]
	elif is_list(a) and is_num(b):
		yield a + [b]
	elif is_str(a) and is_list(b):
		yield b + [a]
	elif is_list(a) and is_str(b):
		yield a + [b]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def increase_array_element_yield(a, b, arg):
	if is_int(a) and is_list(b):
		b[a % len(b)] += 1
		yield b
	elif is_list(a) and is_int(b):
		a[b % len(a)] += 1
		yield a
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def decrease_array_element_yield(a, b, arg):
	if is_int(a) and is_list(b):
		b[a % len(b)] -= 1
		yield b
	elif is_list(a) and is_int(b):
		a[b % len(a)] -= 1
		yield a
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_divisible_yield(a, b, arg):
	if is_int(a) and is_int(b):
		yield int(a%b == 0)
	elif is_int(a) and is_list(b):
		yield [int(a%n == 0) for n in b]
	elif is_list(a) and is_int(b):
		yield [int(n%b == 0) for n in a]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def add(a, b):
	return a+b

def mult(a, b, arg):
	return a*b
