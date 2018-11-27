from check_type import *
import math
import itertools

def get_list_or_string_item_or_concatenate_yield(a, b, arg):
	if is_int(a) and is_int(b):
		yield int(str(a)+str(b))
	elif is_int(a) and is_list(b):
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
	elif type(a) == type(b) and type(a) != str:
		yield int(a == b)
	elif is_list(a):
		yield a.index(b) if b in a else -1
	elif is_list(b):
		yield b.index(a) if a in b else -1
	elif is_str(a) and is_str(b):
		if (len(a) == 1 or len(b) == 1) and len(a) != len(b):
			if len(a) < len(b):
				yield b.find(a)
			else:
				yield a.find(b)
		else:
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
	elif is_int(a) and is_str(b):
		yield ''.join([b[i%len(b)] for i in range(a)])
	elif is_str(a) and is_int(b):
		yield ''.join([a[i%len(a)] for i in range(b)])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_greater(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a > b)
	elif is_int(a) and is_list(b):
		yield [b[i] for i in range((a+1)%len(b), len(b))]
	elif is_list(a) and is_int(b):
		yield [a[i] for i in range((b+1)%len(a), len(a))]
	elif is_int(a) and is_str(b):
		yield ''.join([b[i] for i in range((a+1)%len(b), len(b))])
	elif is_str(a) and is_int(b):
		yield ''.join([a[i] for i in range((b+1)%len(a), len(a))])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_leq(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a <= b)
	elif is_int(a) and is_list(b):
		yield [b[i%len(b)] for i in range(a+1)]
	elif is_list(a) and is_int(b):
		yield [a[i%len(a)] for i in range(b+1)]
	elif is_int(a) and is_str(b):
		yield ''.join([b[i%len(b)] for i in range(a+1)])
	elif is_str(a) and is_int(b):
		yield ''.join([a[i%len(a)] for i in range(b+1)])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_geq(a, b, arg):
	if is_num(a) and is_num(b):
		yield int(a >= b)
	elif is_int(a) and is_list(b):
		yield [b[i] for i in range(a%len(b), len(b))]
	elif is_list(a) and is_int(b):
		yield [a[i] for i in range(b%len(a), len(a))]
	elif is_int(a) and is_str(b):
		yield ''.join([b[i] for i in range(a%len(b), len(b))])
	elif is_str(a) and is_int(b):
		yield ''.join([a[i] for i in range(b%len(a), len(a))])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def is_not(a, b, arg):
	if type(a) == type(b):
		yield int(a != b)
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def zip_yield(a, b, arg):
	if is_list(a) and is_list(b):
		max_len = max(len(a), len(b))
		yield [([a[i]] if i<len(a) else []) + ([b[i]] if i<len(b) else []) \
		for i in range(max_len)]
	elif is_str(a) and is_str(b):
		max_len = max(len(a), len(b))
		yield "".join([(a[i] if i<len(a) else "") + (b[i] if i<len(b) else "") \
		for i in range(max_len)])
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def add_yield(a, b, arg):
	if is_num(a) and is_num(b):
		yield a+b
	# elif is_num(a) and is_list(b):
		# yield [n+a for n in b]
	# elif is_list(a) and is_num(b):
		# yield [n+b for n in a]
	elif is_list(a) and is_list(b):
		yield a+b
	elif is_str(a) and is_num(b):
		yield a+str(b)
	elif is_num(a) and is_str(b):
		yield str(a)+b
	elif is_list(a):
		yield [c for n in a for c in add_yield(n, b, arg)]
	elif is_list(b):
		yield [c for n in b for c in add_yield(a, n, arg)]
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

def reverse_multiply_yield(a, b, arg):
	for res in mult_yield(b, a, arg):
		yield res

def divide_yield(a, b, arg):
	if is_int(a) and is_int(b):
		yield a//b
	elif is_num(a) and is_num(b):
		yield a/b
	elif is_num(a) and is_list(b):
		yield [a//n if is_int(a) and is_int(n) else a/n for n in b]
	elif is_list(a) and is_num(b):
		yield [n//b if is_int(b) and is_int(n) else n/b for n in a]
	elif is_list(a) and is_list(b):
		yield [n2 for n2 in b if n2 not in set([n for n in a if n not in set(b)])]
	elif is_str(a) and is_int(b):
		yield [a[i*b:(i+1)*b] for i in range(math.ceil(len(a)/b))]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def reverse_divide_yield(a, b, arg):
	for res in divide_yield(b, a, arg):
		yield res

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
	elif is_str(a) and is_num(b):
		yield str(b) + a
	elif is_num(a) and is_str(b):
		yield str(a) + b
	elif is_str(a) and is_str(b):
		yield b + a
	elif is_int(a) and is_int(b):
		yield int(str(b)+str(a))
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
	elif is_str(a) and is_num(b):
		yield a + str(b)
	elif is_num(a) and is_str(b):
		yield b + str(a)
	elif is_str(a) and is_str(b):
		yield a + b
	elif is_int(a) and is_int(b):
		yield int(str(a)+str(b))
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

def center_string_or_int_yield(a, b, arg):
	if is_int(a) and is_int(b):
		yield str(a).center(b)
	elif is_int(a) and is_str(b):
		yield b.center(a)
	elif is_str(a) and is_int(b):
		yield a.center(b)
	elif is_int(a) and is_list(b):
		yield [str(n).center(a) for n in b]
	elif is_list(a) and is_int(b):
		yield [str(n).center(b) for n in a]
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def pad_to_equal_length(a, b, arg):
	if is_list(a) and (is_int(b) or is_str(b)):
		max_len = 0
		for n in a:
			max_len = max(max_len, len(str(n)))
		res = []
		for n in a:
			pad = max_len - len(str(n))
			res.append(pad*str(b)+str(n))
		yield res
	elif is_list(b) and (is_int(a) or is_str(a)):
		max_len = 0
		for n in b:
			max_len = max(max_len, len(str(n)))
		res = []
		for n in b:
			pad = max_len - len(str(n))
			res.append(pad*str(a)+str(n))
		yield res
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def contains_yield(a, b, arg):
	if is_list(a):
		yield 1 if b in a else 0
	elif is_list(b):
		yield 1 if a in b else 0
	elif is_str(a):
		yield 1 if str(b) in a else 0
	elif is_str(b):
		yield 1 if str(a) in b else 0
	elif is_int(a) and is_int(b):
		yield 1 if str(b) in str(a) else 0
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))

def inclusive_range_yield(a, b, arg):
	if is_int(a) and is_int(b):
		if b < a:
			yield list(range(b, a+1))
		else:
			yield list(range(b, a-1, -1))
	else:
		raise ValueError("[%s][%s]%s is not supported" % (type(a), type(b), arg.char))
