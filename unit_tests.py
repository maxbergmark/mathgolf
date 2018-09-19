from subprocess import check_output
from code_page import *

def run_program(code, input_string = ""):
	with open("unittest.mg", "w") as f:
		f.write(code)
	compile_command = "python3 pre_processor.py unittest.mg"
	run_command = "echo \"%s\" | python3 math_golf.py --unittest unittest.out" % input_string
	total_call = ";".join([compile_command, run_command])
	return check_output(total_call, shell = True).decode('utf-8')[:-1]

programs = [
	"♀{î╕Σ╠δ╕┌╠δ`+Γî35α÷ä§p",
	"k▒hrzúm*ç'+u",
	"k─²Σ°",
	"k╫k╨]",
	"êgÅΣ°",
	"ID",
	"'$W∙",
	"kÅ■┐▲î ",
	"kórg¶",
	"k55+;",
	"k╒⌂*n",
	"5º*♪{k[K∞╟(]m<Σ∞wΦ}*σ",
	"k3<k3≤k3>k3=k3≥k3¡",
	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
	"☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕",
	"k!k#♪%)",
	"0123456789]2/2-",
	"123?",
	"123@",
	"123\\",
	"1_2∙3·4abcd9rf",
	"eπτφ",
	"j3*ilo_q[2431]s[243]z",
	"tv9rw",
	"êx",
	"\"[123]\"~_£¥ª",
	"\"abcdef«\"abcdef»",
	"1234⌐567¬89",
	"12345]24µ03lµ",
	"k∞_4÷¿¼½",
	"êmÄ_mÅ_+mÉ∞_+mæ__++mÆ_∙+++mô∙∙++++mö∙__++++mò____++++",
	"123456789αßΓ",
	"kâ_ä_à_å",
	"ëè",
	"5r2*{[ïíì]q;",
	"5rñkñ\"123\"ña",
	"ûabùabcÿabcd]",
	"12345]2Θⁿε+",
	"9r~Äq↑9r~Äq↓9r~Äq→9r~Äq←9r~Äq∟9r~Äq↔9r~Äq▲9r~Äq▼",
	"k⌠9√=⌡",
	"k┐q└q_┴q┬",
	"5┘5┌0┘0┌[012]┘[012]┌\"\"┘\"\"┌",
	"12345]├\\┤",
	"╢a╖ab╕ab╣a║ab╗ab",
	"[21354]╙[21354]╓45╙45╓'a'b╙'a'b╓",
	"╟╚╔",
	"12345]╞_q╡",
	"k╤∞╥╦╩a╩b╩c",
	"k╪kr╪\"abc\"╪",
	"123451263]▀1▌2▐",
	"k░a kr░"

]

inputs = [
	[""],
	["123", "10203"],
	["41", "42"],
	["10", "511", "512"],
	["1 4 9 16 25 1111", "1431 2 0 22 999999999", "22228 4 113125 22345", "", "421337 99 123456789 1133557799"],
	[""],
	[""],
	["2", "16", "5", "7"],
	["1", "2", "3", "4"],
	["1", "2", "3", "4"],
	["1", "2", "3", "4"],
	["0", "44", "45", "59", "60", "100"],
	["1", "2", "3", "4"],
	[""],
	[""],
	["1", "2", "3", "4"],
	[""],
	[""],
	[""],
	[""],
	[""],
	[""],
	["5.4 \'hej\'"],
	[""],
	["1 3 2 4 3 5 4 6"],
	[""],
	[""],
	[""],
	["\'abcdefghijkl\'"],
	["1", "2", "3", "4", "5"],
	["1 2 3 4 5"],
	[""],
	["1", "2", "3", "4"],
	["1 2 3", "1.5 2.5 3.5"],
	[""],
	["1234"],
	[""],
	[""],
	[""],
	["0", "1", "2", "3", "4"],
	["-2", "-1", "0", "1", "2"],
	[""],
	[""],
	[""],
	[""],
	[""],
	[""],
	["1", "2", "3", "4", "5"],
	["1", "2", "3", "4", "5"],
	[""],
	["1", "2", "3", "4"]
]
outputs = [
	["1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"],
	["100+20+3", "10000+200+3"],
	["0", "1"],
	["[5, 16]", "[511, 512]", "[1, 1024]"],
	["[1, 4, 9, 1111]", "[1431, 0, 22, 999999999]", "[22228, 4, 22345]", "[]", "[]"],
	["2014"],
	["$353535"],
	["1", "4", "5", "16"],
	["[]", "[2, 3]", "[2, 3, 5, 7]", "[2, 3, 5, 7, 11, 13]"],
	["1", "2", "3", "4"],
	["*\n", "*\n**\n", "*\n**\n***\n", "*\n**\n***\n****\n"],
	["['1000', '', '', '', '']", "['1000', '', '', '', '']", "['326', '328', '346', '', '']", "['326', '328', '346', '', '']", "['199', '189', '204', '191', '217']", "['199', '189', '204', '191', '217']"],
	["110001", "110001", "010110", "001011"],
	["1112131415171819202122232425262728293031333435363738"],
	["16326412825651210242048409610100100010000100000100000010000000100000000"],
	["2", "5", "217", "777"],
	["[-2, -2, -1, -1, 0, 0, 1, 1, 2, 2]"],
	["231"],
	["312"],
	["132"],
	["112223333[4]-1-2-3[0, 1, 1, 2, 3, 5, 8, 13, 21]"],
	["2.7182818284590453.1415926535897936.2831853071795861.618033988749895"],
	["hej\nhej16hej[1, 2, 3, 4][4, 3, 2]"],
	["150000000000011329033644"],
	["[6, 4, 5, 3, 4, 2, 3, 1]"],
	["[1, 2, 3]1[1]"],
	["stsasosisnssxwxyxmxvxkxx"],
	["723415689"],
	["[1, 2, 5, 4, 3]dbcaefghijkl"],
	["1", "1", "3", "2", "5"],
	["[12000, 12000, 24000, 24000, 36000, 36000, 48000, 48000, 60000, 60000]"],
	["12[3, 4, 5, [6, 7, [8, 9]]]"],
	["[1]111", "[0, 1]2102", "[1, 1]3113", "[0, 0, 1]41004"],
	["[1.0, 2.0, 3.0]['1', '2', '3']", "[1.5, 2.5, 3.5]['1.5', '2.5', '3.5']"],
	["[0, 5, 0][1, 5, 2][2, 5, 4][3, 5, 6][4, 5, 8]"],
	["[0, 1, 2, 3, 4, 3, 2, 1, 0]1234321['12321']"],
	["['ab', 'abc', 'abcd']"],
	["206"],
	["87654321753187654321886420642080012345678012345670123456"],
	["-2", "-1", "-2", "-2", "-2"],
	["-3-100", "-2000", "-1101", "0210", "1300"],
	["1001[0, 1, 1][1, 0, 0]01"],
	["1[2, 3, 4]5"],
	["ststsstsaxwxwxxwxy"],
	["5154ba"],
	["60360086400"],
	["[2, 3, 4, 5][2, 3, 4]"],
	["['and', 'the', 'and']seeusover", "['a', 'and', 'the', 'and', 'a']seeusover", "['a', 'a', 'and', 'the', 'and', 'a', 'a']seeusover", "['was', 'a', 'a', 'and', 'the', 'and', 'a', 'a', 'was']seeusover", "['was', 'was', 'a', 'a', 'and', 'the', 'and', 'a', 'a', 'was', 'was']seeusover"],
	["1[0]cab", "1[1, 0]cab", "3[2, 0, 1]cab", "2[3, 0, 1, 2]cab", "6[4, 0, 1, 2, 3]cab"],
	["[1, 1, 2, 3, 4, 5, 6, 2]"],
	["['1'] ['0']", "['2'] ['0', '1']", "['3'] ['0', '1', '2']", "['4'] ['0', '1', '2', '3']"]
]

# start = 22
# end = 23
# programs = programs[start:end]
# inputs = inputs[start:end]
# outputs = outputs[start:end]

failure = False
errors = []

all_chars_tested = set(''.join(programs))

print("\n\tPerforming %d tests..." % sum(len(i) for i in inputs), end="\n\t")

if len(programs) != len(inputs) or len(programs) != len(outputs):
	print("The inputs and outputs do not match with the program count (%d/%d/%d)" % (len(programs), len(inputs), len(outputs)), end="\n\t")
	quit()

counter = 0
test_count = 0
for program, inps, outps in zip(programs, inputs, outputs):
	if len(inps) != len(outps):
		print("\n\tThere should be as many inputs as there are outputs", end="\n\t")
		failure = True
		break
	for inp, outp in zip(inps, outps):
		program_output = run_program(program, inp)
		if counter > 0 and counter % 40 == 0:
			print("", end="\n\t", flush=True)
		if not program_output == outp:
			failure = True
			print("F", end="", flush=True)
			errors.append("%d: (%s) (%s) Failed asserting that \"%s\" == \"%s\"" % (test_count, program, inp, program_output, outp))
		else:
			print(".", end="", flush=True)
		counter += 1
	test_count += 1

if not failure:
	print("\n\tAll unit tests passed!", end="\n\t")
else:
	print()
	for error in errors:
		print(error)

untested_chars = set(code_page) - set(unused_chars) - all_chars_tested

if len(untested_chars) > 0:
	print("Total untested characters: (%d/255) %s" % (len(untested_chars), ''.join(sorted(list(untested_chars)))))
else:
	print("All characters have been tested!")