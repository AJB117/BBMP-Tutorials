
# 2 - Variables

## [Previous (Anatomy of a program)](./anatomy-of-a-program.md)

## Purpose

If a program is just a bunch of procedures acting on data, we'd better have a way to store data. Variables are way for programs to store data. We can store anything: a bunch of characters like "Good morning", numbers, complex data structures, and (crucially) other variables.

## Types

Every variable has a **type** according to what kind of data it can hold. A **type system** is a hierarchy of types that governs which types are sub-types of others. While Python and JavaScript are what are called [dynamically typed languages](https://en.wikipedia.org/wiki/Dynamic_programming_language), they still use a type system under the hood. Dart, on the other hand, is a statically typed language.

The difference is that, in a dynamically typed language, data types of variables can be determined while the program is running, and programmers need not specify what type each variable is while writing their program. A statically typed language is the opposite; loosely speaking, data types must be specified at the time of writing the program.

Why is there this distinction? Typically, it's easier to write quick and dirty programs in a dynamically typed language than a statically typed one. However, programs written in statically typed languages are often faster due to optimizations that can only be made assuming that the type of a variable is known at compile-time.

Below are some example data types that most languages have, and what they represent. It should be noted, however, that not all languages have these types. Fortunately, Python, JavaScript, and Dart have a lot of overlap in what types data can be.

| Type | What it represents |
| ----------- | ----------- |
| `int`      | Whole number (integer) |
| `float` | Floating point number (decimal number) |
| `double` | Higher precision float |
| `bool`   | True/false |
| `char` | Character (e.g. 'c') |
| `string` | String (a bunch of characters, e.g. "Hello!") |
| `object` | Bascially, a custom type made up of the above primitive types. We'll cover this in the [classes](./classes.md) section|

Different languages have different types and ways of treating their types, but these are the main types you'll see across different languages.

### Your turn

Let's set some variables and print them. The name of the file you should put the code in is in the top [comment](https://en.wikipedia.org/wiki/Comment_(computer_programming)).

### Python

```python
# variables-1.py
number = 4
word = "word"
boolean = True

print(number)
print(word)
print(boolean)
```

Notice that in Python, variable initialization is super simple. It's just `<variable name> = <value>`.

Run with `python3 variables-1.py` in the directory you wrote `variables-1.py`.

### JavaScript

```javascript
// variables-1.js
let number = 4;
let word = "word";
let bool = true;

console.log(number);
console.log(word);
console.log(boolean);
```

Notice that in JavaScript, we initialize a variable with `<modifier> <variable name> = <value>`. We'll talk more about modifiers below, but it's basically a keyword to specify how you want JavaScript to allocate memory.

Run with `node variables-1.js` in the directory you wrote `variables-1.js`.

### Dart

```dart
// variables-1.dart
void main() {
    int number = 4;
    String word = "word";
    bool boolean = true;

    print(number);
    print(word);
    print(boolean);
}
```

Notice that in Dart, the syntax to initialize a variable is `<data type> <variable name> = <value>` where `<value>` must be of type that matches `<data type>`. For instance, you'll get an error if you try to run the program writing `int number = 4.5` since `number` is declared as an integer but was set to a floating point number.

Run with `flutter run variable-1.dart` in the directory you wrote `variable-1.dart`.

Play with the above demos until you're comfortable with variables. Notice that Dart is the only language that has types in each variable initialization. This is because it is statically typed, and it will throw a fit if you mismatch a variable's type and value.

Try setting variables equal to each other and seeing what happens.

## Initialization vs Declaration

What we did above was variable **initialization**, not declaration. **Declaration** is where memory is made for a variable, but no value is set. For instance, in JavaScript, you're allowed to write

```JavaScript
let variable;
```

Essentially, most languages let you ommit the `=` in an initialization for variable declaration. In Python, however, you must initialize every variable. The closest you can get is to just make a variable equal to `None` (read more [here](https://realpython.com/null-in-python/)).

```Python
variable = None
```

## Modifiers

A modifier is a way to specify how the computer should declare/initialize a variable. This is most noticeable in JavaScript and Dart. For example, a variable declared `const` in `JavaScript` is **read-only**; it cannot be reassigned. For instance,

```JavaScript
const a = 0;
a = 1; // this code will break
```

The equivalent in Dart is `final`.

```dart
final a = 0;
a = 4; // this code will break
```

Why would this be useful? Well, a lot of bugs in programming occur because data pops up where it shouldn't. Namely, a variable is assigned incorrectly, or a variable's data changes without the programmer realizing it. `const` and `final` help eliminate the possibility for this. Of course, this means you can't reassign variables once they've been initialized, meaning you'll probably have to make a new variable each time you want to manipulate data.

Python has no such modifier keyword. In fact, it has no modifier keywords.

There are other modifier keywords, especially in Dart, but you can go research them yourself. Just know they exist and when they might be good to use.

## [Next (functions)](./functions.md)
