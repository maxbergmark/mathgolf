from code_page import *

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
		bracket_counter = 0
		while (bracket_counter > 0 or temp.char != "}") and code:
			if temp.char == "{":
				bracket_counter += 1
			if temp.char == "}":
				bracket_counter -= 1
			c.append(temp)
			temp = code.pop()
		if not code and temp.char != "}":
			c.append(temp)

		c = c[::-1]
	return c, code

def for_looping(n):
	for i in range(n):
		yield i