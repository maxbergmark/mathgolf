from subprocess import check_output
from code_page import *

def run_program(code, input_string = ""):
	with open("unittest.mg", "w") as f:
		f.write(code)
	compile_command = "python3 pre_processor.py unittest.mg"
	run_command = "echo \"%s\" | python3 math_golf.py --unittest unittest.out" % input_string
	total_call = ";".join([compile_command, run_command])
	return check_output(total_call, shell = True).decode('utf-8')

data = [
	"♀{î╕Σ╠δ╕┌╠δ`+Γî35α÷ä§p",
		[""],
		["1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"],
	"k▒hrzúm*ç'+u",
		["123", "10203"],
		["100+20+3", "10000+200+3"],
	"k─²Σ°",
		["41", "42"],
		["0", "1"],
	"k╫k╨]",
		["10", "511", "512"],
		["[5, 16]", "[511, 512]", "[1, 1024]"],
	"gÅΣ°",
		["[1,4,9,16,25,1111]", "[1431,2,0,22,999999999]", "[22228,4,113125,22345]", "[]", "[421337,99,123456789,1133557799]"],
		["[1, 4, 9, 1111]", "[1431, 0, 22, 999999999]", "[22228, 4, 22345]", "[]", "[]"],
	"ID",
		[""],
		["2014"],
	"'$W∙",
		[""],
		["$353535"],
	"kÅ■┐▲î ",
		["2", "16", "5", "7"],
		["1", "4", "5", "16"],
	"kórg¶",
		["1", "2", "3", "4"],
		["[]", "[2, 3]", "[2, 3, 5, 7]", "[2, 3, 5, 7, 11, 13]"],
	"k55+;",
		["1", "2", "3", "4"],
		["1", "2", "3", "4"],
	"k╒⌂*n",
		["1", "2", "3", "4"],
		["*", "*\n**", "*\n**\n***", "*\n**\n***\n****"],
	"5º*♪{k[K∞╟(]m<Σ∞wΦ}*σ",
		["0", "44", "45", "59", "60", "100"],
		["['1000', '', '', '', '']", "['1000', '', '', '', '']", "['326', '328', '346', '', '']", "['326', '328', '346', '', '']", "['199', '189', '204', '191', '217']", "['199', '189', '204', '191', '217']"],
	"k3<k3≤k3>k3=k3≥k3¡",
		["1", "2", "3", "4"],
		["110001", "110001", "010110", "001011"],
	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
		[""],
		["1112131415171819202122232425262728293031333435363738"],
	"☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕",
		[""],
		["16326412825651210242048409610100100010000100000100000010000000100000000"],
	"k!k#♪%)",
		["1", "2", "3", "4"],
		["2", "5", "217", "777"],
	"0123456789]2/2-",
		[""],
		["[-2, -2, -1, -1, 0, 0, 1, 1, 2, 2]"],
	"123?",
		[""],
		["231"],
	"123@",
		[""],
		["312"],
	"123\\",
		[""],
		["132"],
	"1_2∙3·4abcd9rf",
		[""],
		["112223333[4]-1-2-3[0, 1, 1, 2, 3, 5, 8, 13, 21]"],
	"eπτφ",
		[""],
		["2.7182818284590453.1415926535897936.2831853071795861.618033988749895"],
	"j3*ilo_q[2431]s[243]z",
		["5.4 \'hej\'"],
		["hej\nhej16hej[1, 2, 3, 4][4, 3, 2]"],
	"tv9rw",
		[""],
		["150000000000011329033644"],
	"êx",
		["1 3 2 4 3 5 4 6"],
		["[6, 4, 5, 3, 4, 2, 3, 1]"],
	"\"[123]\"~_£¥ª",
		[""],
		["[1, 2, 3]1[1]"],
	"\"abcdef«\"abcdef»",
		[""],
		["stsasosisnssxwxyxmxvxkxx"],
	"1234⌐567¬89",
		[""],
		["723415689"],
	"12345]24µ03lµ",
		["\'abcdefghijkl\'"],
		["[1, 2, 5, 4, 3]dbcaefghijkl"],
	"k∞_4÷¿¼½",
		["1", "2", "3", "4", "5"],
		["1", "1", "3", "2", "5"],
	"êmÄ_mÅ_+mÉ∞_+mæ__++mÆ_∙+++mô∙∙++++mö∙__++++mò____++++",
		["1 2 3 4 5"],
		["[12000, 12000, 24000, 24000, 36000, 36000, 48000, 48000, 60000, 60000]"],
	"123456789αßΓ",
		[""],
		["12[3, 4, 5, [6, 7, [8, 9]]]"],
	"kâ_ä_à_å",
		["1", "2", "3", "4"],
		["[1]111", "[0, 1]2102", "[1, 1]3113", "[0, 0, 1]41004"],
	"ëè",
		["1 2 3", "1.5 2.5 3.5"],
		["[1.0, 2.0, 3.0]['1', '2', '3']", "[1.5, 2.5, 3.5]['1.5', '2.5', '3.5']"],
	"5r2*{[ïíì]q;",
		[""],
		["[0, 5, 0][1, 5, 2][2, 5, 4][3, 5, 6][4, 5, 8]"],
	"5rñkñ\"123\"ña",
		["1234"],
		["[0, 1, 2, 3, 4, 3, 2, 1, 0]1234321['12321']"],
	"ûabùabcÿabcd]",
		[""],
		["['ab', 'abc', 'abcd']"],
	"12345]2Θⁿε+",
		[""],
		["206"],
	"9r~Äq↑9r~Äq↓9r~Äq→9r~Äq←9r~Äq∟9r~Äq↔9r~Äq▲9r~Äq▼",
		[""],
		["87654321753187654321886420642080012345678012345670123456"],
	"k⌠9√=⌡",
		["0", "1", "2", "3", "4"],
		["-2", "-1", "-2", "-2", "-2"],
	"k┐q└q_┴q┬",
		["-2", "-1", "0", "1", "2"],
		["-3-100", "-2000", "-1101", "0210", "1300"],
	"5┘5┌0┘0┌[012]┘[012]┌\"\"┘\"\"┌",
		[""],
		["1001[0, 1, 1][1, 0, 0]01"],
	"12345]├\\┤",
		[""],
		["1[2, 3, 4]5"],
	"╢a╖ab╕ab╣a║ab╗ab",
		[""],
		["ststsstsaxwxwxxwxy"],
	"[21354]╙[21354]╓45╙45╓'a'b╙'a'b╓[]╙[]╓123",
		[""],
		["5154ba123"],
	"╟╚╔",
		[""],
		["60360086400"],
	"12345]╞_q╡",
		[""],
		["[2, 3, 4, 5][2, 3, 4]"],
	"k╤∞╥╦╩a╩b╩c",
		["1", "2", "3", "4", "5"],
		["['and', 'the', 'and']seeusover", "['a', 'and', 'the', 'and', 'a']seeusover", "['a', 'a', 'and', 'the', 'and', 'a', 'a']seeusover", "['was', 'a', 'a', 'and', 'the', 'and', 'a', 'a', 'was']seeusover", "['was', 'was', 'a', 'a', 'and', 'the', 'and', 'a', 'a', 'was', 'was']seeusover"],
	"k╪kr╪\"abc\"╪",
		["1", "2", "3", "4", "5"],
		["1[0]cab", "1[1, 0]cab", "3[2, 0, 1]cab", "2[3, 0, 1, 2]cab", "6[4, 0, 1, 2, 3]cab"],
	"123451263]▀1▌2▐",
		[""],
		["[1, 1, 2, 3, 4, 5, 6, 2]"],
	"k░a kr░",
		["1", "2", "3", "4"],
		["['1'] ['0']", "['2'] ['0', '1']", "['3'] ['0', '1', '2']", "['4'] ['0', '1', '2', '3']"],
	"Wr\\-╓",
		["[0,1,2,3]", "[1]", "[0,1,3,4]"],
		["4", "0", "2"],
	"æî_ \\;",
		["1", "2", "3", "4"],
		["1 ", "1 12 ", "1 12 23 ", "1 12 23 34 "],
	"ÆÅ_╞↑ ",
		["['Hello','world']", "['Darth','vader']"],
		["Helloellolloloo worldorldrldldd ", "Dartharthrththh vaderaderdererr "],
	"▀=",
		["[1,2,3]", "[3,2,1]", "[1,2,2]", "[2,2,2]"],
		["1", "1", "0", "0"],
	"{{îq}}",
		["3", "4", "5 3", "2 3 4"],
		["112", "112123", "1121231234", "1"],
	"§§]",
		["3", "3 4", "3 4 5", "3 4 5 6"],
		["[333]", "[343]", "[543]", "[543]"],
	"=¿{=¿{\"t t\"}{\"t f\"}}{=¿{\"f t\"}{\"f f\"}}",
		["5", "5 4", "5 5", "5 4 3", "5 5 4", "5 5 5", "5 5 5 5", "5 4 5 5", "5 4 5 4", "5 4 4 5", "5 4 4 4", "5 4 3 2"],
		["t t", "f f", "t t", "f f", "t f", "t t", "t t", "f t", "f f", "f f", "f t", "f f"],
	"╜{'fq}╛{'tq}",
		["0", "1", "[0]", "[0,1]", "5 0", "0 5"],
		["f", "t", "f", "t", "", "ft"],
	"╜q╛q",
		["0", "1", "2", "0 2", "2 0", "0 0", "2 2", "2 3", "3 2"],
		["0", "1", "2", "2", "", "0", "2", "2", "3"],
	"9rá{3%",
		[""],
		["[0, 3, 6, 1, 4, 7, 2, 5, 8]"],
	"9rá{¶",
		[""],
		["[0, 1, 4, 6, 8, 2, 3, 5, 7]"],
	"9rá¥",
		[""],
		["[0, 2, 4, 6, 8, 1, 3, 5, 7]"],
	"Æ)_Σk=▼",
		["2", "8", "12", "16", "18", "24", "32"],
		["11", "17", "39", "79", "99", "699", "5999"],
	"2*",
		["123", "123\n234", "1\n23\n456"],
		["246", "246\n468", "2\n46\n912"],
	"123┼",
		[""],
		["1232"],
	"0♫ô4ƒ²)/+♫/",
		[""],
		["3.145093388791592"],
	"♀╒g{2╧┌",
		[""],
		["[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100]"],
	"m{ïìî}",
		["'123'", "'abc'", "'defghi'"],
		["101121223233", "a0a1b1b2c2c3", "d0d1e1e2f2f3g3g4h4h5i5i6"],
	"g{;ï¥",
		["'abcdefghijklmnop'"],
		["bdfhjlnp"],
	"g=",
		["'abcdefghijkl' '_b_d_f_h_j_l'"],
		["bdfhjl"],
	"±",
		["5", "-5", "1.23", "-1.23", "[1,2,-3]", "[-1,-2,-3]"],
		["5", "5", "1.23", "1.23", "[1, 2, 3]", "[1, 2, 3]"],
	"_)_(_⌠_⌡",
		["'abc'", "'defg'", "'a'", "123", "['a','abc',123]"],
		["abcbcdabccdeabc", "defgefghdefgfghidefg", "abaca", "123124123125123", "['a', 'abc', 123]['b', 'bcd', 124]['a', 'abc', 123]['c', 'cde', 125]['a', 'abc', 123]"],
	"└┐",
		["'abc'", "'defg'", "'a'", "123", "['a','abc',123]"],
		["abcbcdabc", "defgefghdefg", "aba", "123124123", "['a', '`', 'b', 'a', 'abc', '`ab', 'bcd', 'abc', 123, 122, 124, 123]"],
	"ÿ∞'ÿ▌∞'ÿ▌",
		[""],
		["ÿ∞'ÿ▌∞'ÿ▌"],
	"ÿ_'ÿ¬_'ÿ¬",
		[""],
		["ÿ_'ÿ¬_'ÿ¬"],
	"WÉƒ²)]4╠▓",
		[""],
		["3.2958603789455028"],
	"5{)q}3{)q}[246]{)q}",
		[""],
		["12345123357"],
	"{)q",
		["5", "[2,4,6]"],
		["12345", "357"],
	"♀╒ÇÅ2╧",
		[""],
		["[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100]"],
	"y]",
		["[1,2,3]", "[0,5,4]", "[1,'2',3,'4']", "['a','b','c']", "['ab','cd','ef']", "['ab',12,'cd',34]"],
		["[123]", "[54]", "[1234]", "['abc']", "['abcdef']", "['ab12cd34']"],
	"$",
		["'ABCD'","'A'", "'a'", "98", "66", "123456"],
		["1145258561", "65", "97", "b", "B", "@Γ☺"],
	"$$",
		["'ABCD'","'A'", "'a'"],
		["ABCD", "A", "a"],
	".",
		["'ABC' 5","5 'ABC'", "[1,2,3] 5", "5 [1,2,3]"],
		["ABCABCABCABCABC", "ABCABCABCABCABC", "[5, 10, 15]", "[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]"],
	"│", 
		["[1,2,3,4,5]", "[2,3,5,7,11]", "[9,1,8,2,7,3,6,4,5]"],
		["[1, 1, 1, 1]", "[1, 2, 2, 4]", "[-8, 7, -6, 5, -4, 3, -2, 1]"],
	"▄_a",
		[""],
		["abcdefghijklmnopqrstuvwxyz['abcdefghijklmnopqrstuvwxyz']"],
	"3@",
		["2 1", "1"],
		["312", "311"],
	"3?",
		["2 1", "1"],
		["231", "131"],
	"^",
		["[1,2,3,4,5] [1,2,3,4,5]", "[1,2,3,4,5] [2,3,4,5,1]", "[1,2,3,4,5] []", "[1,2,3,4,5] [1,2,3]"],
		["[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]", "[[2, 1], [3, 2], [4, 3], [5, 4], [1, 5]]", "[[1], [2], [3], [4], [5]]", "[[1, 1], [2, 2], [3, 3], [4], [5]]"],
	"123[432]r╘",
		[""],
		[""],
	"Åïq↨",
		["1 5", "3 8", "6 2"],
		["12345", "345678", "65432"],
	"93Åïq↨",
		[""],
		["3456789"]
]

programs = data[::3]
inputs = data[1::3]
outputs = data[2::3]

start = len(programs)-2
end = len(programs)
programs = programs[start:end]
inputs = inputs[start:end]
outputs = outputs[start:end]

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