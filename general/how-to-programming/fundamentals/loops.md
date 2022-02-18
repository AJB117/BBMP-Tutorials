# Loops

## [Previous (functions)](./functions.md)

## Purpose

Often, you'll want to execute some function or body of code multiple times or until a condition is met. But you don't want to be like [this guy](https://youtu.be/oiNPgJmtzVI?t=91) and copy and paste the same snippet of code as many times as needed. We should be smart and use loops.

## For loops

A loop is just a way to repeat some body of code. A for loop is a counter-based construction that iteratively checks when a counter variable has hit a certain bound. Below are programs that print the first 10 multiples of 2.

### Python

```python
for i in range(10):
    print(i*2)
```

For loops in Python are very easy, although it does not use the usual counter construction described above. In this code snippet, `range` returns a sequence of numbers from 0 to 9 (not 10; `range` goes up to the number you give it minus one). The `i` is a variable made on the fly that takes on the value of each number in the sequence provided by `range`.

### JavaScript

```js
for (let i = 0; i < 10; i++) {
    console.log(i*2);
}
```

For loops in JavaScript are more wordy. Let's break it down.

`let i = 0;`: this initializes a loop counter variable to 0.
`i < 10;`: this is the condition on which the loop will stop. That is, the loop will halt when `i` >= 10.
`i++`: this increments `i` by 1.

Until `i` is greater than or equal to 10, the code in the curly braces will keep running, and `i` will keep incrementing.

### Dart

```dart
void main() {
    for (int i = 0; i < 10; i++) {
        print(i*2);
    }
}
```

The Dart way of making for loops is basically the same as JavaScript's except we must declare our counter `i` as an integer.

## While loops

Sometimes, we want to repeat an action until some non-numerical condition is met. Imagine we have a function `disasterReport` that returns `true` 50% of the time and `false` the other 50% of the time, and we want to repeat some code until `disasterReport` returns `true`.

### Python

```python
def keep_living():
    print('nothing to see here...')

disaster_has_struck = disasterReport()
while not disaster_has_struck:
    keep_living()
    disaster_has_struck = disasterReport()

print('Everything is in shambles')
```

### JavaScript

```js
function keepLiving() {
    console.log('nothing to see here...');
}

disasterHasStruck = disasterReport();
while (!disasterHasStruck) {
    keepLiving();
    disasterHasStruck = disasterReport();
}
console.log('Everything is in shambles')
```

### Dart

```dart
void keepLiving() {
    print("nothing to see here...");
}

void main() {
    bool disasterHasStruck = disasterReport();
    while (!disasterHasStruck) {
        keepLiving();
        disasterHasStruck = disasterReport();
    }
    print("Everything is in shambles");
}
```

Recall that the `!` operator negates the logical value of the variable next to it. In Python, we use the `not` operator instead. We see that while loops in the above languages are all largely the same; they're comprised of the keyword `while` followed by some condition. When that condition is met, the loop stops. Otherwise, it keeps executing its body.

Notice we have to keep updating the `disasterHasStruck` variable in each example inside of the while loop body. If we didn't, we'd have a 50% chance of having an infinite loop on our hands, and that'd be terrible.

Interestingly, it turns out it's impossible to write a program that can tell you whether an arbitrary (key word) program will terminate or loop forever ([the halting problem](https://en.wikipedia.org/wiki/Halting_problem)).

## Continue and break

If you want to, for some reason, skip through an iteration of a loop or completely exit a loop, use the `continue` and `break` keywords. In Python,

```python
for i in range(10):
    if i % 2 == 0:
        break       # we exit the whole loop when i is even

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)        # print only the odd numbers
```

## A Python point

Notice we have to keep updating `disasterHasStruck` to see whether the while loop can terminate. In Python, there's a handy thing called the [walrus operator](https://realpython.com/python-walrus-operator/) that eliminates the need to initialize disasterHasStruck and keep updating it. Can you update `walrus.py` in this directory using the walrus operator?

## Exercises

1. It is known that, in at least the languages above, any for loop can be rewritten as a while loop. Write a program using a for loop that takes a user inputted number `n`, and prints the cube of that number `n` times. Then, rewrite it using a while loop.
2. Write a function that calculates the nth Fibonacci number.