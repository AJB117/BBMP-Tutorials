# 1 - Anatomy of a program

## Syntax

What does a program usually look like?

Typically, a program is just a bunch of **data structures** being acted on by a bunch of **functions**. A data structure is just something that holds data, and a function is a procedure that takes input, processes the input, and produces some output. Every program can be thought of as a composition of some functions.

More generally, a program is just a text file that a machine runs according to what language it is written in. A compiler and interpreter are just programs that transform that text into actionable instructions for the computer to execute.

The rules governing how a programming language is written is called **syntax**. Writing code without syntax errors is a rite of passage everyone goes through; practice makes perfect. There will be a point where learning another programming language will become much easier as you grow accustomed to programming.

As we learn to program, keep in mind the syntax being used. Instead of copying and pasting the examples in these tutorials, try to copy the examples by hand. It will help build muscle memory in writing syntactically correct programs.

Below are some common syntactical trends in programming languages. You may not understand all the terms, but it should be useful after you finish the general tutorial as.

| Syntactical pattern      | What it does |
| ----------- | ----------- |
| `blah()`      | Function call |
| `blah.thing()` | Method call |
| `;`   | End of line, a single statement        |
| `blah {...}` | Code block/scope |
| `=` | Assignment |
| `=>` or `->` | Anonymous function |
| `blah.thing` | Class/instance member |

## Operators

I wasn't sure where to put this section, but I think it fits here. In nearly all languages, there are some basic operators that are useful for everyone. An **operator** is just a symbol used for performing a certain action between some other symbols in the language.

| Operator | What it does | How to use it|
| ----------- | ----------- |--- |
| `+, -, *, /`      | Addition, subtraction, multiplication, division| `a _ b` where `_` is just one of the ops |
| `%` | Modulo (remainder, e.g. 4 % 5 = 1) | `a % b` |
| `++`   | Increment (not in Python) | `a++` |
| `+=, -=, *=, /=, %=` | Execute operator and then assign (e.g. `a += 4` means add 4 to `a`) | `a _= b` where `_` is just one of the ops
| `&&, ||` | Logical [AND](https://en.wikipedia.org/wiki/Logical_conjunction), logical [OR](https://en.wikipedia.org/wiki/Logical_disjunction) (in Python, it's `and` and `or`)| `a && b`, `a || b` |
| `>`, `<` | Greater than, less than| `a > b`, `a < b` |
| `!` | Logical negation (converts true to false and vice versa) | `!a` |
| `!=` | Is not equal to | `a != b` |
| `==` | Is equal to | `a == b`|

## [Next (variables)](./variables.md)
