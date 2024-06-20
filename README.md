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
- __init__ -> You can initialise a package using __init__.py file, this allows you to use the package from any other directory in the program.
