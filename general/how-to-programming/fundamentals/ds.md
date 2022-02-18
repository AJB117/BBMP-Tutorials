# Essential Data Structures

## [Previous (control flow)](./control-flow.md)

## Purpose

I mentioned programming is about data and acting on that data. Well, there's more to data than just variables. A **data structure** is any structure that holds data. Certain data structures have better properties than others, e.g. better faster access time, faster insertion time, etc. Data structures are not hardware constructions; they are abstract, implemented by other programs. A big part of computer science is designing data structures that are efficient.

## Arrays/Lists

Arrays and (linked) lists are probably the most common data structures. Simply put, they are used when you want to store a sequential collection of data.

Here's the difference between an array and a linked list for most programming languages: an array's values are stored contiguously in memory while a linked list's values can be stored anywhere in memory.

When you store data in an array, each data element is stored side-by-side in the computer's memory. To get data from an array, you must **index** the array. An index is just a number representing which element of the array you want. For instance, suppose we have an array `arr = [1, 2, 3, 4]`. Then `arr[0] = 1`, `arr[1] = 2`, `arr[3] = 4`, and so on. Note our array indices start at 0.

On the other hand, when you store data in a linked list, most languages typically store each data element in **nodes** which are like little packets of data containing 2 things: (1) the data element itself and (2) a **pointer** to the next packet in the linked list. This pointer is the memory address of the next element of the linked list. Using this pointer strategy, a linked list's contents need not be contiguous; its values can be dispersed in memory.

This is a simplification of what is otherwise a fundamental topic in beginning data structures. It would be a good idea to get an idea of when is better than the other.

In programming, Python and JavaScript don't really give the programmer an option as to which data structure to use. They're called lists in Python and arrays in JavaScript. However, under the hood, Python implements its lists using arrays, and I'm pretty sure JavaScript uses a [hashmap](https://en.wikipedia.org/wiki/Hash_table) instead. I'm not sure what Dart uses under the hood, but they call their constructs lists like in Python.

What's important to know is that both arrays and lists are ordered and used with indexing.

To practice, say we have a list of numbers whose even numbers we want to return.

### Python

```python
def get_evens(arr):
    evens = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        return evens

arr = [1, 2, 3, 4, 5]
print(get_evens(arr))
```

Notice that in Python, we initialize a list using square brackets, and we use `.append` to add a value to the end of the list. See docs [here](https://docs.python.org/3/tutorial/datastructures.html) for more things you can do with a list.

### JavaScript

```javascript
function getEvens(arr) {
    const evens = [];
    for (let i = 0; i < arr.length; i++) {
        const value = arr[i];
        if (value % 2 === 0) {
            evens.push(value);
        }
    }
    return evens;
}

arr = [1, 2, 3, 4, 5];
console.log(getEvens(arr));
```

As you might expect by now, JavaScript's version is quite verbose. Let's break it down.

`const evens = [];` We initialize an array to which we'll add even numbers.

`for ...` We loop over the array given to `getEvens`.

`const value = arr[i];` We call the `i`th value of the input array `value`.

`if (value % 2 == 0)` We check for evenness.

`evens.push(value)` We add `value` to our list of evens.

You can find more stuff to do with an array in JS [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

### Dart

```dart
List<int> getEvens(List<int> arr) {
    List<int> evens = [];
    for (int i = 0; i < arr.length; i++) {
        int value = arr[i];
        if (value % 2 == 0) {
            evens.add(value);
        }
    }
}
void main() {
    List<int> arr = [1, 2, 3, 4, 5];
    print(getEvens(arr));
}
```

The Dart implementation is basically the same as the JavaScript one with 2 caveats. First, notice we type `getEvens`, `arr`, and `evens` with `List<int>`. `List` is a class, or abstract data type, which we'll learn about later, and it itself accepts a data type (here, it's `int`). Typing a variable with `List<int>` means that the variable being typed is a list of integers. Second, Dart's way of adding data to lists is with `add` instead of Python's `append` or JS's `push`. See [here](https://api.dart.dev/stable/2.16.1/dart-core/List-class.html) for more stuff you can do with Dart lists.

## Hash tables

So arrays/lists are nice if you want a sequential list of values. You can imagine it'd be very useful for modeling data in, say, a productivity app where each person's todo list is an array.

However, there are other times where we want to correspond certain **keys** with **values**. For example, what if we wanted to count how many times every word occurs in a string? We can't dynamically create variables. Arrays, while they'd work if we were counting characters (see [ASCII](https://www.asciitable.com/)), will not help us here. Hash tables to the rescue.

Simplified, a hash table is just a lookup table. A hash table is called a hash table because it associates [hashed](https://en.wikipedia.org/wiki/Hash_function) keys with certain values. An ideal hash function will give a perfect mapping from keys to values. However, this is very difficult, and no hashing function is perfect. Practically speaking, we can ignore this imperfection and act like there is no problem.

An advantage of hash tables is that they can associate non-integers with any kind of data. While one can make a list of, say, strings, each index of the array must be an integer. The keys or "indices" of a hash table can be nearly anything, subject to the programming language you're using.

Implementing our word-counting program, suppose our string is "hello goodbye goodbye good morning".

### Python

```python
string = "hello goodbye goodbye good morning"
counts = {}
for word in string.split(' '):
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

Python uses [dictionaries](https://realpython.com/python-dicts/) instead of hash maps, but the principle is the same: key-value pairs.

`counts = {}` We initialize a dictionary called `counts`.

`for word in string.split(' ')` We take our string and split it by each space. The output is a list of strings, i.e. the words in the string.

`counts[word] = counts.get(word, 0) + 1` We'd like to write `counts[word] += 1`, but some keys are not in the dictionary, and so their values are not initialized. Using `.get(key, default)` on a dictionary attempts to get the value at key `key`, and if it is not in the dictionary already, it returns the default value `default`. So here, we are updating `counts[word]` to be whatever was stored there previously plus 1 if `word` is already in `counts`. Otherwise, `counts[word]` is equal to 0 + 1 = 1. Read on [here](https://realpython.com/python-dicts/) for more info on `.get`.

### JavaScript

```js
const string = "hello goodbye goodbye good morning";
const counts = {};
const words = string.split(" ");
for (let i = 0; i < words.length; i++) {
    const word = words[i];
    const value = counts[word];
    counts[word] = value ? value + 1 : 1;
}
console.log(counts);
```

There are actually 2 things you can use for hash maps in JavaScript: the [object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), and the [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map). There are advantages to both, but objects are more convenient and multipurpose.

`const counts = {};` This is the same as in the Python program, except we're initializing an object.

`const words = string.split(" ");` Same as in the Python program.

`const value = counts[word]` We get whatever the object has in store for the key `word`. Notice that it could be `undefined` if `word` is not in `counts` yet.

`counts[word] = value ? value + 1 : 1;` Here we use a ternary operator. If `value` is `undefined`, that means `word` isn't in `counts` yet, so we should set `counts[word]` to 1 since its the first time we've seen `word`. Otherwise, we should increment whatever is at `counts[word]`.

### Dart

```dart
void main() {
  String string = "hello goodbye goodbye good morning";
  List<String> words = string.split(" ");
  Map<String, int> counts = {};

  for (int i = 0 ; i < words.length; i++) {
    String word = words[i];
    if (counts[word] == null) {
      counts[word] = 1;
    } else {
        counts[word] = counts[word]! + 1;
    }
  }
  print(counts);
}
```

This is very similar to the JS case. The obvious difference is that we do an explicit `null` check. Also, in Dart, `Map` is a class like `List` and accepts 2 types: the type of the key and the key of the value per key-value pair. Here, we use `Map<String, int>` because our key-value pairs associate strings with integers.

In the `else` block, we write `counts[word] = counts[word]! + 1` because Dart types the values of maps are **optional**, meaning they could be null. However, since we check in the `if` block whether `counts[word]` is null, we can tell the compiler to ignore the possible null case and force our way into incrementing `counts[word]` using the `!` operator. Notice the use of `!` here is different from the logical operator `!`. To negate a logical value, put `!` before a variable/value. To tell the compiler to ignore a null check, put `!` after the variable/value.

You would be right to think that this is risky practice, and it is. Avoid this as much as possible. There are more "Darty" ways of writing such this program.

## Exercises

1. Rewrite your Fibonacci program, except using arrays/lists. While it won't make your program any more memory efficient, it employs [memoization](https://en.wikipedia.org/wiki/Memoization), which is useful for more complicated problems.
2. Given a string, count the occurrence of each character in the string and print that count. Don't use the code we've written in the hash tables section; use arrays. Recall ASCII (hint: an array/list can be thought of as a special case of a hash table).
3. Solve [Two Sum](https://leetcode.com/problems/two-sum/) using a hash table (hint: subtraction is your friend).

## [Next (sharing code)](./sharing-code.md)
