
import re
from subprocess import check_output




def run_program(code, input_string = ""):
	with open("unittest.mg", "w") as f:
		# print(code)
		f.write(code)
		f.close()
	compile_command = "python3 pre_processor.py unittest.mg"
	run_command = "echo '%s' | python3 math_golf.py unittest.out" % input_string
	total_call = ";".join([compile_command, run_command])
	# print(total_call)
	return check_output(total_call, shell = True).decode('utf-8')[:-1]












programs = [
	"♀{î╕Σ╠δ╕┌╠δ`+Γî35α÷ä§p",
	"k▒hrzúm*ç'+u",
	"k─²Σ°",
	"k╫k╨]",
	"êgÅΣ°",
	"ID",
	"'$W∙"
]
inputs = [
	[""],
	["123", "10203"],
	["41", "42"],
	["10", "511", "512"],
	["1 4 9 16 25 1111", "1431 2 0 22 999999999", "22228 4 113125 22345", "", "421337 99 123456789 1133557799"],
	[""],
	[""]
]
outputs = [
	["1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"],
	["100+20+3", "10000+200+3"],
	["0", "1"],
	["[5, 16]", "[511, 512]", "[1, 1024]"],
	["[1, 4, 9, 1111]", "[1431, 0, 22, 999999999]", "[22228, 4, 22345]", "[]", "[]"],
	["2014"],
	["$353535"]
]

failure = False

print("Performing %d tests..." % sum(len(i) for i in inputs))

for program, inps, outps in zip(programs, inputs, outputs):
	if len(inps) != len(outps):
		print("\nThere should be as many inputs as there are outputs")
		failure = True
		break
	for inp, outp in zip(inps, outps):
		program_output = run_program(program, inp)
		if not program_output == outp:
			failure = True
			print("F", end="", flush=True)
		else:
			print(".", end="", flush=True)

if not failure:
	print("\nAll unit tests passed!")