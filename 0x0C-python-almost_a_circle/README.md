unittest, args/kwargs, JSON encoder and decoder

## Unit Testing in a Large Project

**Definition:** Unit testing is a software testing method where individual units or components of a software are tested independently.

**Implementation:**
1. Choose a testing framework (e.g., pytest, unittest).
2. Write test cases for each unit.
3. Automate tests to run during development or integration.

## Serialization and Deserialization of a Class

**Serialization:** Process of converting a class instance to a byte stream.

**Deserialization:** Process of reconstructing a class instance from a byte stream.

**Implementation:**
```python
import pickle

# Serialization
serialized_data = pickle.dumps(obj)

# Deserialization
obj = pickle.loads(serialized_data)
```

## Writing and Reading a JSON File

**Writing:**
```python
import json

data = {"key": "value"}
with open("file.json", "w") as json_file:
    json.dump(data, json_file)
```

**Reading:**
```python
with open("file.json", "r") as json_file:
    data = json.load(json_file)
```

## *args and **kwargs in Python

**`*args`:**
- Used to pass a variable number of non-keyword arguments to a function.
- Example:
  ```python
  def example_func(*args):
      print(args)
  ```

**`**kwargs`:**
- Used to pass a variable number of keyword arguments to a function.
- Example:
  ```python
  def example_func(**kwargs):
      print(kwargs)
  ```

## Handling Named Arguments in a Function

```python
def example_func(name, age):
    print(f"Name: {name}, Age: {age}")

# Call the function with named arguments
example_func(name="John", age=25)
```
