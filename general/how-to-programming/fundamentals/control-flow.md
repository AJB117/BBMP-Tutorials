# Control flow

## [Previous (loops)](./loops.md)

## Purpose

We can store data, we can write functions, and we can execute code multiple times. But what if we want to execute different code depending on some condition? That's where control flow statements come in.

## If/else

The most common way for a language to let a programmer do different things based on some value is with the if/else construction.

Say we want to write a function that divides 2 numbers. However, as we all know, dividing anything by 0 is undefined <sup>[1](#myfootnote1)</sup>.

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


## Exercises

<a name="myfootnote1">1</a>: Footnote content goes here

## [Next (Essential data structures)](./ds.md)

---

1. [Anatomy of a program](./fundamentals/anatomy-of-a-program.md)
2. [Variables](./fundamentals/variables.md)
3. [Functions](./fundamentals/functions.md)
4. [Loops](./fundamentals/loops.md)
5. [Control flow](./fundamentals/control-flow.md)
6. [Essential data structures](./fundamentals/ds.md)
7. [Sharing code](./fundamentals/sharing-code.md)
8. [Classes](./fundamentals/classes.md)
9. [More functions](./fundamentals/more-functions.md)