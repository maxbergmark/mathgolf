import sys
from code_page import *

ibm437_visible = lambda byt: code_page.index(byt)

script = open(sys.argv[1], "r").read().replace("\n", "")
byts = bytearray([ibm437_visible(s) for s in script])

output_file = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1].split(".")[0]+".out"
output = open(output_file, "wb")
output.write(byts)