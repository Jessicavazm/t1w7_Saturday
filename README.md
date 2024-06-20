# t1w7_Saturday

# Wildcard Argument
```
    Wildcard arguments allow functions to accept a variable number of arguments. This is often done using *args and **kwargs.
    *args = used by position / stores a sequence
    **kwargs = using by the name / stores both the key and the value
```
- When you don't know how many arguments the function will have, very useful for when you don't know the number of args.
- Non-keyword arguments *args (they use the argument positional). First item goes to first argument, second item goes to second argument and goes on.
- Keyword arguments (name = value, so if you invert the order it won't matter). Very similar to dictionary. 

# Modules
- One of the techniques for following DRY Coding Principles 
- Group similar code and functions together in a separate file
- Solves the problem of code file being to lengthy and complex
- Can be reused across several programs
- Python comes with a lot of modules as well called Python Standard Library

# Packages
- Collection of modules
- Organise related modules under one directory
- __init__ -> You can initialise a package using __init__.py file, this allows you to use the package from any other directory in the program. Init also helps to not write the name of the module, once packaged is initialised you just need to call the package.

## Practical example
Task:
- Create a package for basic text processing with modules for:
    - Counting words in a string
    - Counting characters in a string and,
    - Reversing strings

# Slicing a sequence 
- Way to extract parts of data structures from strings,lists, tuples.
- Syntax: sequence[start:stop:step] ---> similar to range. 
- Default of start:0 , default of step is 1.

### Text processing folder
- A folder with modules, __init__ was used to help to extract those modules and be able to use them outside the text_processing folder. 

# Object Oriented Programming
- It is a way to help programmers structure the functionality of your program that would make sense to
humans and would allow computers to run it efficiently. 
- Almost all programming languages uses this concept
- It uses "objects" to model real-world entities.

## Key Concepts
- Class
    - A blueprint for creating objects.
    - It defines a set of attributes or methods that the created objects (instances) will have
    - Eg. Blueprint provided while building a house, defining what an animal is.
    
- Objects
    - Using a class you build objects.
    - An instance of a class.
    - It represents a specific entity with attributes (data) and methods (functions) which are defined by the class.
    - Eg. A built house with many features (as function)
    - Eg: class_eg(Dog)
    - Eg: BankAccount

