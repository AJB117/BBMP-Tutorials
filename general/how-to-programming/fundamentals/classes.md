# 7 - Classes

## [Previous (Essential data structures)](./ds)

## Purpose

In a previous section, we talked about data types. Classes and objects are topics related to types in that they describe how you can create your own "types," commonly called "abstract data types."

Let's say I want to make a to-do list app. I might want to model my data as a list of to-do items where each item has a title, a due date, and a tag/category. One way we can do this is by using arrays, one for holding titles, another for due dates, and another for tags/categories. In other words, we can make `titles_arr[i]` hold the `i`th title and `due_date_arr[i]` hold the `i`th due date. This is a headache to work with since all your data is strewn all over the place.

A better way to model this data is with a **class**. Now you don't have to use a class; other languages have things like **structs** (C, C++, Swift, Rust) or **objects** (JavaScript, Scala) in addition to classes. But the key point is that classes and their cousins help you accomplish a key point: encapsulating data with behavior.

Coming back to our to-do list example, we can model each to-do item like so (in Dart, to illustrate):

```dart
class ToDoItem {
    String title;
    Date dueDate;
    List<String> tags;
}
```

This is much nicer than the array approach; now we can declare a variable like `List<ToDoItem> todos` that holds all three relevant data to a to-do item instead of having to index 3 arrays.

Notice that the `ToDoItem`'s `dueDate` **property** is of tyep **Date**. A nice feature of classes is that, in most languages, you can nest them however deep you want. You can have classes with properties that are also classes.

I mentioned earlier that classes encapsulate data and behavior. The above example shows how it captures data, but what about behavior, i.e., functions? Suppose we want every to-do item to be able to return a list of tags starting with the letter "e". We do it like so:

```dart
class ToDoItem {
    String title;
    Date dueDate;
    List<String> tags;

    String[] getTagsStartingWithE() {
        return this.tags.where((tag) => tag.startsWith('e')).toList()
    }
}
```

Ignore the content of `getTagsStartingWithE`; we'll talk about that next section. The point is that we can bundle behavior as well as data in a single class. We call functions within a class a **method**.

What if we wanted to initialize a `ToDoItem` with default values? That's where **constructors** come in. A constructor is just a method that initializes some properties of the class.

```dart
class ToDoItem {
    String title;
    Date dueDate;
    List<String> tags;

    String[] getTagsStartingWithE() {
        return this.tags.where((tag) => tag.startsWith('e')).toList()
    }

    ToDoItem(this.title, this.dueDate, this.tags)
}
```

Every language has a different way of writing a constructor, but the basic idea is the same. Every constructor takes an argument for its properties and initializes it to a value given by the user.

Here's how we can use a class, putting it all together:

```dart
class ToDoItem {
    String title;
    Date dueDate;
    List<String> tags;

    String[] getTagsStartingWithE() {
        return this.tags.where((tag) => tag.startsWith('e')).toList()
    }

    ToDoItem(this.title, this.dueDate, this.tags)
}

class Date {
    int year;
    int month;
    int day;
    Date(this.year, this.month, this.day)
}

void main() {
    Date date = Date(1, 3, 4)
    List<String> tags = ["eel-catching", "gen chem", "electronics"];
    ToDoItem todo = ToDoItem("title", date, tags);

    print(todo.title); // outputs "title"
    print(todo.tags);  // outputs ["electricity & magnetism", "gen chem", "electronics"]
    print(todo.dueDate);  // what does this output?

    print(todo.getTagsStartingWithE()); // outputs ["eel-catching", "electronics"
}
```

Pretty much universally, the `this` keyword represents the current instance variable. Think of a class as a blueprint that gives structure to a blob of data. When you **instantiate** a class, like in `ToDoItem todo = ToDoItem(...)`, then we say `todo` is an **instance** of the class `ToDoItem`. The `this` keyword, within `todo`, refers to itself. Note that this means every instance of every class has a different piece of memory pointed to by `this`. We also call instances **objects** in most circumstances.

Now in other languages.

### Python

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class ToDoItem:
    def __init__(self, title, due_date, tags):
        self.title = title
        self.due_date = due_date
        self.tags = tags
    def getTagsStartingWithE(self):
        return [tag for tag in self.tags if tag[0] == 'e']

date = Date(1, 3, 4)
tags = ["eel-catching", "gen chem", "electronics"]
todo = ToDoItem("title", date, tags)

print(todo.title)
print(todo.tags)
print(todo.dueDate)

print(todo.getTagsStartingWithE())
```

Notice that in Python, we use `self` instead of `this`. Also, the `this` keyword isn't automatically defined within the class; if any method in a class in Python wants to access its instance's properties, it must accept `self` as a first parameter. Further, a constructor in Python is defined by the `__init__` method.

### JavaScript

```js
class Date {
    constructor(year, month, day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }
}

class ToDoItem {
    constructor(title, dueDate, tags) {
        this.title = title;
        this.dueDate = dueDate;
        this.tags = tags;
    }
    getTagsStartingWithE() {
        return this.tags.filter((tag) => tag[0] === 'e');
    }
}

const date = new Date(1, 3, 4);
const tags = ["eel-catching", "gen chem", "electronics"];
const todo = new ToDoItem("title", date, tags);

console.log(todo.title)
console.log(todo.tags)
console.log(todo.dueDate)

console.log(todo.getTagsStartingWithE())
```

JavaScript takes a more traditional approach to constructors with a clearly defined method called `constructor`.

Classes are an extremely rich subject. It would be good to read up on as much as you can on classes and any other related concepts in your language of choice.

- [Python](https://docs.python.org/3/tutorial/classes.html)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Dart](https://dart.dev/guides/language/language-tour#classes)

## Exercises

1. Model a game of tic-tac-toe using classes. You don't need to make a working game (although that's the best way to learn!), but you should get used to thinking in terms of classes and objects.
2. Look up **inheritance** for your programming language of choice. Implement an example. Also read up on **composition**, especially if you're into JavaScript. Generally speaking, most developers prefer to work with composition over inheritance. How come?

## [Next (more functions)](./more-functions.md)
