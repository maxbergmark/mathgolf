def is_str(n):
	return type(n) is str

def is_num(n):
	return type(n) is int or type(n) is float

def is_int(n):
	return type(n) is int

def is_int_string(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float_string(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_list(n):
	return type(n) is list

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
