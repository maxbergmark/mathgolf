# MathGolf

This is the git repo for my golfing language. It is still in early development, so any feedback is appreciated.

## Usage

It is written in python, and uses [Code page 437](https://en.wikipedia.org/wiki/Code_page_437) to visualize the program.

Programs are run using:

        echo "input as string" | python3 math_golf.py program.mg


## Data types

The data types in this language are `float`, `int`, `list` and `string`. They are all internally represented by Python's data types, which makes the line between `float` and `int` somewhat fuzzy.

## Why MathGolf

MathGolf is heavily centered around mathematical golfing challenges, with many builtins to handle arithmetics and array manipulations. It also has a wide choice of 1-byte number inputs, making number input easier.

On top of that, a lot of mapping and functions are implicitly mapped to each element of an array, meaning that explicit mapping should hopefully be a rare occurrence.

## Examples

### Hello, world!

	"Hello, world!

`"` starts a string. With no closing quote, the string is implicitly closed when the code ends.

### Print ascii triangle of asterisk

Here we will take an integer as input, and print a triangle to standard output of the desired size.

	k╒'**n

#### Input

	5

#### Output

	*
	**
	***
	****
	*****

#### Explanation

	k         Read integer from standard input
	 ╒         Create list(range(1, a+1))
	  '* 	Push asterisk as single character string
	    * 	Multiply string and list with implicit mapping
	     n 	Implicit '\n'.join(a) and output

### FizzBuzz

	♀{îÿfizzÿbuzz`+Γî35α÷ä§p}*

#### Explanation

	♀                           Push 100
	 {                          Start block
	  î                         Push loop counter (1-indexed)
	   ÿfizz                    Push "fizz"
	        ÿbuzz               Push "buzz"
	             `              Duplicate top 2 elements of stack
	              +             Add (creating "fizzbuzz")
	               Γ            Wrap top 4 elements of stack in array
	                î           Push loop counter (1-indexed)
	                 3          Push 3
	                  5         Push 5
	                   α        Wrap last 2 elements in array
	                    ÷       Check divisibility (implicit mapping)
	                     ä      Convert from binary to int
	                      §     Get array item
	                       p    print
	                        }*  End block, "*" means for loop