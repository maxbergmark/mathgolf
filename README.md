# MathGolf

## News

With the latest changes, these new operators have been added:

### Auto golfing

I have added a rudimentary script for auto-golfing. It will only work for shorter challenges, up to 3 bytes in practice. You can input test cases, and then run every possible program of a certain length to see if there's a combination of operators which satisfy all test cases. I'll continue working on this, making it more useful. Right now I'd only recommend using it if you know that a short (<5 byte) solution exists, and you want to be sure that no shorter solution exists.  

### `ü` ceiling operator

This operator works just like expected. It works for all numericals and lists of numericals, where it maps implicitly.

This is the git repo for my golfing language. It is still in early development, so any feedback is appreciated.

### `^` zip operator

This operator zips together two lists. If input is `[1,2,3]` and `[4,5]`, the result is `[[1,4],[2,5],[3]]`

### `↨` range(a,b) loop or list

This character defined that the loop should pop two integers from the stack, and loops from the first to the second (inclusive).

For example, the program `74Åïq↨` outputs `4567`. The reason for the reverse order is that input is read left to right but stack values are read top to bottom, and I prioritised preserving input order rather than stack order.

You can also use it as an operator, where it also consumes two arguments from the stack or input, and pushes `list(range(a,b+1))` or `list(range(a,b-1,1))` to the stack depending on the size of a and b.

### `│` difference operator

Right now it only works with lists of numbers. With input `[a,b,c,d,e]`, it creates the list `[b-a,c-b,d-c,e-d]`.

### `.` reverse multiplication operator

Reverses the order of the two arguments, and sends them to the multiply function. Helpful when you're multiplying numbers with lists, which can either repeat the list or implicitly map to the list depending on multiplication order. Saves a byte compared to `\*` (swap elements and multiply)

### `,` reverse subtraction operator

Same as the reverse multiplication, useful for skipping the swapping of elements. 

### `▄` lowercase alphabet

The entire lowercase alphabet (a-z) as a string. 

### `$` `ord(a)` or `char(a)`

Depending on if `a` is a string or an integer, it converts it to the other. The mapping is bijective, meaning that `$$` becomes the null operator for strings and integers. This operator is helpful for easily creating large numbers using strings, where it basically works like base-256 notation. 

Right now I'm working on customizing the code page for MathGolf so that it includes 256 characters. Since CP437 includes the null character, and two different space characters, I might change two characters in the future (null and non breaking space) into more readable characters. It shouldn't affect a large number of current programs.

## Usage

It is written in python, and uses [Code page 437](https://en.wikipedia.org/wiki/Code_page_437) to visualize the program.

### Compiling

To compile your script into a file with appropriate byte count, take your utf-8 encoded file and compile it using:

    python3 pre_processor.py program.mg

This will create the file `program.out`, which has the same byte count as the length of your script.

### Execution

Scripts are executed using either

    echo "input as string" | python3 math_golf.py program.out

or

    python3 math_golf.py program.out < input.txt

## Input

All input is evaluated using `ast.literal_eval`. Thus, strings should be quoted with `'`, lists should be input as `[1,2,3]`, and floats/ints are input as is.

To run a test suite, or test your script for multiple inputs, provide each input on a separate line.

## Data types

The data types in this language are `float`, `int`, `list` and `string`. They are all internally represented by Python's data types, which makes the line between `float` and `int` somewhat fuzzy. I have tried to make sure that operators don't change the data type unexpectedly.

## Why MathGolf

MathGolf is heavily centered around mathematical golfing challenges, with many builtins to handle arithmetics and array manipulations. It also has a wide choice of 1-byte number inputs, making number input easier.

On top of that, a lot of mapping and functions are implicitly mapped to each element of an array, meaning that explicit mapping should hopefully be a rare occurrence.

## Flags

### Debug `-d`

This flag helps with understanding what the code does. It prints all executed commands in order, along with the stack content after said command has been executed. The print is executed after the command itself has been executed, which means that loop handlers and nested commands can be printed in an unexpected order.

### Slow execution `-s`

Please don't use this flag on TIO. It won't destroy anything, but it makes your script take a lot longer to run, especially if you have loops. It adds a 0.1 second delay after each command, which can be useful in combination with the `-d` flag for debugging. 

### Generate code explanation `-e`

This is a new function, and it's a work in progress. But if you want rudimentary explanations for what your code does, you can add the `-e` flag. Then the code is not executed, but instead a markdown explanation is printed to stdout. Since this feature is in development, it might not include some of the newer operators. It also doesn't work properly for strings, something that I might fix in the future. 

#### Example

This example uses the same code as the ascii triangle example below. 

    $ python3 pre_processor.py test_program.mg; python3 math_golf.py test_program.out -e
    
    ╒      range(1,n+1)
     ⌂     asterisk character (for challenges where a printable character is needed)
      *    pop a, b : push(a*b)
       n   newline char, or map array with newlines


## Examples

### Hello, world!

    "Hello, world!

`"` starts a string. With no closing quote, the string is implicitly closed when the code ends.

### Hello, world! (golfed)

    'H╕○ô╣·╩Θ'!

    This code is three bytes shorter. It uses MathGolf's shorthands for compressed strings, fixed-length strings and the dictionary to encode "Hello, world!"

#### Explanation

    'H             Push "H"
      ╕○ô          Decompress "○ô" to get "ello"
         ╣·        Decompress "·" to get ", "
           ╩Θ      Access top 256 words in dictionary to get "world"
             '!    Push "!"


### Print ascii triangle of asterisk

Here we will take an integer as input, and print a triangle to standard output of the desired size.

    ╒⌂*n

#### Input

    5

#### Output

    *
    **
    ***
    ****
    *****

#### Explanation

          Read integer from standard input (implicit)
    ╒     Create list(range(1, a+1))
     ⌂    Push an asterisk
      *   Multiply string and list with implicit mapping
       n  Implicit '\n'.join(a) and output

### FizzBuzz

    ♀{î╕Σ╠δ╕┌╠δ`+Γî35α÷ä§p

#### Explanation

    ♀                         Push 100
     {                        Start block
      î                       Push loop counter (1-indexed)
       ╕Σ╠δ                   Decompress "Σ╠" and capitalize to get "Fizz"
           ╕┌╠δ               Decompress "┌╠" and capitalize to get "Buzz"
               `              Duplicate top 2 elements of stack
                +             Add (creating "FizzBuzz")
                 Γ            Wrap top 4 elements of stack in array
                  î           Push loop counter (1-indexed)
                   3          Push 3
                    5         Push 5
                     α        Wrap last 2 elements in array
                      ÷       Check divisibility (implicit mapping)
                       ä      Convert from binary to int
                        §     Get array item
                         p    print
                              Block is implicitly ended, for/foreach is the default behavior