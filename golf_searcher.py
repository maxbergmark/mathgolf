from code_page import *
from math_golf import *
import signal
from itertools import product
import resource
import time

def estimate_remaining(elapsed, progress, total):
	total_time = int(elapsed*(total/progress - 1))
	time_string = []
	if total_time > 3600:
		time_string.append("%2dh" % (total_time // 3600,))
		total_time %= 3600
	if total_time > 60:
		time_string.append("%2dm" % (total_time // 60,))
		total_time %= 60
	time_string.append("%2ds" % total_time)

	return " ".join(time_string)

def signal_handler(signum, frame):
	raise TimeoutError("Timed out!")

def check_int():
	if is_int_string(res_str):
		if abs(int(res_str) - goal) < abs(best_result - goal):
			best_result = int(res_str)
			best_code = code
			print("New best result:", best_code, best_result)
	# print(print_list(result), end = '\n' if i<len(input_lines)-1 else '')

input_lines = ["7 6 0","5 6 1","8 11 3","1 11 3","2 10 3","11 1 2","6 1 4","12 1 3"]
output_lines = ["0", "1", "1", "1", "0", "1", "0", "1"]
# output_lines = list("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
# input_lines = ["" for _ in output_lines]
corrects = {}

# goal = int(input("Desired output: "))
code_length = int(input("Desired length: "))
best_result = 0
best_code = ""
forbidden = "opq►◄↕()â t↨v~à!☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§ABCDEFGHIJKLMNOPQRSTUVWXYZÄÅÉæÆôöòûùÿ╢╖╕╣║╗╟╚╔óú{}" + "ε*■.r∟→←▲▼↔"
# forbidden = "opqtv►◄☼↕àâ Aaw"
# forbidden = "╒ε*"
# code_page = "╒x%ª+ε*"
# code_page = "{îïíìk\\-+,@?xr(╒┐└01"
code_page_copy = code_page[:]
timeouts = []
exceptions = []
memory_errors = []

for c in forbidden:
	code_page_copy = code_page_copy.replace(c, "")

total_iters = len(code_page_copy)**code_length
all_codes = product(code_page_copy, repeat = code_length)
correct = []

soft, hard = resource.getrlimit(resource.RLIMIT_AS)
resource.setrlimit(resource.RLIMIT_AS, (1*2**30, 2*2**30))
t0 = time.time()
for i, code in enumerate(all_codes):
	code = ('-','±') + code + ('≥',)
	elapsed = time.time() - t0
	est = estimate_remaining(elapsed, i+1, total_iters)
	print("\r\t%6d/%6d: %s %12s" % (i+1, total_iters, ''.join(code), est), end = "")

	commands = [code_page.index(c)+1 for c in code]
	code_list = [Argument(char, c) for char, c in zip(code, commands)][::-1]
	correct_count = 0
	for j, line in enumerate(input_lines):
		signal.signal(signal.SIGVTALRM, signal_handler)
		signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
		stdin = StdIn(line)
		try:
			result = evaluate(code_list[:], stdin, Stack([]))
			res_str = print_list(result)
			if res_str == output_lines[j]:
				if (output_lines[j] not in code):
					corrects[output_lines[j]] = ''.join(code)
			# if res_str == ''.join(code):
			# if 0x20 <= ord(code[0]) <= 0x7e and len(res_str) == 1 and res_str != code[0]:
				correct_count += 1
		except MemoryError:
			memory_errors.append("".join(code))
		except TimeoutError as e:
			timeouts.append("".join(code))
		except Exception as e:
			exceptions.append("".join(code))

	if correct_count == len(input_lines):
		print("\tCorrect code found:", code, res_str, end="", flush=True)
		correct.append(("".join(code), res_str))

print()
print('\n'.join(["%s: %s" % s for s in correct]))
print("Number of correct programs:", len(correct))
print("Exceptions:", len(exceptions))
print("Memory errors:", len(memory_errors))
print("Timeouts:", len(timeouts), timeouts)
# print(timeouts)
print(corrects)