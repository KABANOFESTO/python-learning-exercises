# Python Learning Exercises

A collection of small Python programs created while learning core language features and object-oriented programming.

## Topics covered

- Printing output and basic Python syntax
- `collections.ChainMap` for layered dictionaries
- Recursive Fibonacci sequences
- Classes, instance attributes, and class variables
- Inheritance and the `super()` function
- Method overriding, duck typing, and polymorphism
- Abstract base classes with `abc`

## Project structure

```text
chapter1/
  hello.py              # First Python output
chapter2/
  chainMap.py           # Combining dictionary lookups with ChainMap
oop/
  Animal.py             # Inheritance example
  Car.py, main.py       # Classes and object methods
  Student.py            # Class and instance variables
  Super.py              # Parent constructors with super()
  Polymorphism.py       # Shape implementations
  Duck_Typing.py        # Shared behavior across different objects
  Vehicle.py            # Abstract base class example
problems/
  Fibonacci.py          # Recursive Fibonacci calculator
Dynamic polymorphism.docx
```

## Requirements

- Python 3
- No third-party packages are required.

## Run an example

From the repository root, run a script with Python:

```bash
python chapter1/hello.py
python chapter2/chainMap.py
python problems/Fibonacci.py
python oop/Animal.py
```

`oop/main.py` imports `Car.py`, so run it from the `oop` directory:

```bash
cd oop
python main.py
```

## Purpose

These examples are intended for practice and experimentation. Each file is small and can be run independently, making it easy to explore one Python concept at a time.
