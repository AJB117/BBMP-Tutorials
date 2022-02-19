# How to Program

Programming is the art of telling a computer what to do. Computers are very literal; they do what they are told to the dot, and they have no common sense. This makes programming them a challenge.

While some presentations of programming make programming look like magic, it really isn't. A simple way of thinking about programming is that it's all about taking data from one part of the computer to another. It's all 1s and 0s at the end of the day, after all. Good code moves data efficiently and does exactly what its intended to do while making sense. Bad code moves data inefficiently and shatters some dishware in the process.

Programming is a very collaborative yet independent process. It is collaborative because you'll be using other people's code all the time. It is independent because you'll be responsible for nearly everything your code does, and the problem-solving process involves a lot of self-teaching. Programming has a very low barrier to entry; you don't need any fancy equipment or the latest lab materials to do good work. This plays a powerful role in creating the DIY culture programming communities are known for.

## Programming Languages

A programming language is the language used to tell the computer what to do. As you learn to program, you'll be exposed to many programming languages and therefore many different ways of thinking about solving problems with programming.

You'll often hear people say that your choice of first language to learn is not important, and that after a certain point, all languages feel the same and you'll be able to program anything given a project or two to learn the syntax. This is largely true, but there are some conventions that some languages do better than others, and so your choice of first language will influence how you program in other languages. In these tutorials, we'll be going over 3 languages:

- Python
- JavaScript
- Dart

All three of these are "multi-paradigm". That means they do their best to incorporate conventions from other programming languages into their style.

## Installation

Regardless what kind of development you're interested in, I highly recommend learning at least Python and JavaScript due to their omnipresence. Dart is more framework specific (Flutter), so it's not very generalizable. However, it feels a lot like more popular languages like Java or Kotlin, so learning those languages will probably benefit you more than Dart. The reason these tutorials cover Dart is because they teach how to write apps in Flutter.

### Python (backend dev, ml dev)

For Windows users, try [this](https://docs.python.org/3/using/windows.html) tutorial. You should be able to type in `python3` in a CMD prompt and have the [REPL](https://pythonprogramminglanguage.com/repl/) greet you.

For MacOS/Linux users, your OS should come with Python pre-installed. Just make sure it's not Python 2.x.x. If it is, update it from [here](https://www.python.org/downloads/). You should be able to type in `python3` in a terminal and have the [REPL](https://pythonprogramminglanguage.com/repl/) greet you

### JavaScript (web dev)

Installing JavaScript can be confusing since people have made it possible to run it virtually anywhere.

#### Browser

JavaScript was built for adding interactivity to websites, so every modern browser ships with JavaScript and a [JavaScript engine](https://en.wikipedia.org/wiki/JavaScript_engine#:~:text=A%20JavaScript%20engine%20is%20a%20software%20component%20that%20executes%20JavaScript%20code.&text=In%20a%20browser%2C%20the%20JavaScript,core%20component%20of%20the%20Node.). You can see this by opening your browser's dev tools and typing `console.log("hello world")` into the console. Every browser has a different way of opening dev tools, so be sure to look it up.

#### Not the Browser

The most common way to run JavaScript apart from the browser is with [NodeJS](https://nodejs.org/en/). The official site guides you in how to install NodeJS for your specific OS. Once installed, try typing `node` into a CMD prompt/terminal window to get the Node REPL. Try typing `console.log("hello world")`.

### Dart (mobile dev)

To install Dart, get the [SDK](https://en.wikipedia.org/wiki/Software_development_kit) from the [official site](https://dart.dev/get-dart) which has instructions for your OS. Then, create a file called `hello_world.dart` somewhere with your favorite code editor and type the following into it:

```dart
void main() {
    print('Hello world');
}
```

Save the file and open a CMD prompt/terminal and write `dart run hello_world.dart` in the location of the file `hello_world.dart`. Alternatively, you can install a plugin for your code editor ([one for VSCode](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code), [one for Atom](https://atom.io/packages/dart)) and then use your editor's "Run" button to run the program for you.

There are some programming fundamentals we should cover before delving deeper into the rest of the tutorials.

## Fundamentals

1. [Anatomy of a program](./fundamentals/anatomy-of-a-program.md)
2. [Variables](./fundamentals/variables.md)
3. [Functions](./fundamentals/functions.md)
4. [Loops](./fundamentals/loops.md)
5. [Control flow](./fundamentals/control-flow.md)
6. [Essential data structures](./fundamentals/ds.md)
7. [Sharing code](./fundamentals/sharing-code.md)
8. [Classes](./fundamentals/classes.md)
9. [More functions](./fundamentals/more-functions.md)
