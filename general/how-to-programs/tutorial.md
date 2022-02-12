# Essentials - Git and the Shell

## What's a program?

A program is, simply put, a series of instructions a computer follows to accomplish a task. Those instructions are the code, and there are many steps between the computer reading the code and executing it. These tutorials will not cover these in-between steps; we will focus purely on the code.

Code can run in a lot of contexts, and it largely depends on what the program is trying to accomplish. For instance, a website like Wordle must run on a web browser like Chrome or Safari, or a machine learning model can run anywhere that its programming language and dependencies are supported (e.g. server, desktop app, anywhere really with enough resources). Where the code runs determines a lot about how you write your program. This includes what language you use and what external factors need to be considered (e.g. a desktop app has less of a need to worry about resource management than a program running on a toaster).

## How is code written?

Typically, we want to write code with other people, which begs the question: how do we collaborate on a codebase? The bad way is for everyone to write their version of the program and then share code via email or some cloud service like Google Drive. This is bad because attaching code, downloading code, and seeing where other people made changes in the code becomes very tedious. So, most people use Git.

### Git

Git is a [version control system](https://en.wikipedia.org/wiki/Version_control). It gives structure to how people collaborate on code together, and it's invaluable to a productive team. Instead of everyone doing their own thing and tediously exchanging code bits with each other, Git gives a centralized system that saves different versions of the program and automates the process of sharing, uploading, and reconciling code.

#### Branches

The basic idea of Git is this: there are things called **branches** which are essentially just different versions of a program's codebase. The **main branch** is where a finished product of the program is saved. All other branches are copies of the main branch with various changes. For instance, it's common to have **feature branches** which are branches dedicated to the development of a program feature. Once a developer decides the branch's code should be included in the main branch, they issue a **pull request**, or a request merge their branch into the main branch. This merge usually requires the approval of another programmer or set of programmers.

For example, maybe I'm writing a todo list app, and Alice wants to add a search bar to our app. She would make a new branch apart from main on her own feature branch. Once the search bar is finished, she makes a pull request. Someone else approves this request, and the app now has a search bar.

Note other people can work on Alice's branch as well. However, they would not see any of the changes Alice makes until she **commits** and **pushes** them to the cloud. Similarly, they could only get Alice's changes on her branch by **pulling**.

#### Commits

A commit is a checkpoint in a branch's edit history. 

#### Pushing/Pulling

Note that there is a difference between Git and Github: Git is the program that does all of these magical version control tasks, and Github is just a website built by Microsoft to facilitate the Git workflow. If you wanted to, you could totally make your own git server and set of git tools. If you don't like Github, you can also use services like [Gitlab](https://about.gitlab.com/) or [BitBucket](https://bitbucket.org/product) as well.

#### Installation

Follow [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) guide to install Git for your operating system.
