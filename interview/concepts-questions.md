# Python Important Concepts & Interview Questions

A practical revision guide for Python interviews. Examples use Python 3.

## 1. Core concepts to learn

| Area | Important concepts |
| --- | --- |
| Fundamentals | Variables, objects, types, operators, truthiness, input/output |
| Collections | Strings, lists, tuples, dictionaries, sets, slicing |
| Control flow | Conditions, loops, `break`, `continue`, loop `else` |
| Functions | Arguments, return values, scope, closures, decorators |
| Iteration | Iterables, iterators, generators, comprehensions |
| OOP | Classes, instances, inheritance, composition, polymorphism |
| Reliability | Exceptions, context managers, testing, logging |
| Organization | Modules, packages, imports, virtual environments |
| Advanced | Hashing, copying, memory management, concurrency |
| Problem solving | Frequency counting, two pointers, stacks, searching |

## 2. Python fundamentals

### Q1. What kind of language is Python?

Python is a high-level, dynamically typed, general-purpose language. It supports procedural, object-oriented, and functional programming styles. Indentation defines code blocks.

### Q2. Is Python interpreted or compiled?

In CPython, source code is compiled to bytecode, which is executed by the interpreter. Calling Python only an interpreted language leaves out this compilation step. Other Python implementations can execute code differently.

### Q3. What does dynamically typed mean?

Types belong to objects; a name can be rebound to objects of different types. Python is also strongly typed: it generally does not silently combine incompatible types.

```python
value = 10
value = "ten"              # Rebinding is allowed.
# "10" + 5                 # TypeError
result = int("10") + 5     # Explicit conversion: 15
```

### Q4. What is the difference between mutable and immutable objects?

- **Mutable:** can change in place, such as `list`, `dict`, and `set`.
- **Immutable:** cannot change in place, such as `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

A tuple cannot replace its elements, but an element can itself be mutable.

```python
items = ([1, 2], "python")
items[0].append(3)         # Valid: modifies the nested list.
# items[0] = []            # TypeError: replaces a tuple element.
```

### Q5. What is the difference between `==` and `is`?

`==` compares values, using equality behavior defined by the type. `is` checks whether two references point to the same object. Use `is None` for a `None` check; do not use `is` to compare numbers or strings.

```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b)              # True
print(a is b)              # False
print(a is c)              # True
```

### Q6. Which values are falsy?

Examples include `False`, `None`, numeric zero, and empty collections such as `""`, `[]`, `()`, `{}`, and `set()`. Objects can customize truthiness through `__bool__()` or `__len__()`.

`and` and `or` short-circuit and return operands, not necessarily booleans.

```python
print("" or "default")     # default
print(0 and 100)           # 0
```

### Q7. How do `/`, `//`, and `%` differ?

For integers, `/` produces a float, `//` performs floor division, and `%` gives the remainder. Floor division rounds toward negative infinity.

```python
print(7 / 2)               # 3.5
print(7 // 2)              # 3
print(-7 // 2)             # -4
print(-7 % 2)              # 1
```

### Q8. What is the difference between `None`, `pass`, and `...`?

- `None` is an object representing the absence of a value.
- `pass` is a statement that does nothing, often used for an empty block.
- `...` is the `Ellipsis` object, used in some indexing APIs and as a placeholder.

A function without an explicit return value returns `None`.

## 3. Strings and collections

### Q9. When should you use a list, tuple, set, or dictionary?

| Type | Ordering | Mutable? | Typical use |
| --- | --- | --- | --- |
| `list` | Positional | Yes | A sequence that changes |
| `tuple` | Positional | No | A fixed sequence or record |
| `set` | No guaranteed iteration order | Yes | Unique elements, membership tests |
| `dict` | Insertion order | Yes | Key-value lookup |

Dictionary keys and set elements must be hashable. `{}` creates an empty dictionary; use `set()` for an empty set.

### Q10. What does hashable mean?

A hashable object has a hash value that remains stable during its lifetime, and equal objects must have equal hashes. Hash tables use these properties for lookup.

Strings and integers are hashable. Lists and dictionaries are not. A tuple is hashable only when all its elements are hashable. Immutability and hashability are related but are not interchangeable concepts.

### Q11. How does slicing work?

The syntax is `sequence[start:stop:step]`; the stop position is excluded. Negative indices count from the end. A zero step raises `ValueError`.

```python
numbers = [0, 1, 2, 3, 4]
print(numbers[1:4])        # [1, 2, 3]
print(numbers[::2])        # [0, 2, 4]
print(numbers[::-1])       # [4, 3, 2, 1, 0]
print(numbers[-1])         # 4
```

List slicing creates a shallow copy of the selected elements.

### Q12. How do `append()` and `extend()` differ?

`append(x)` adds one object. `extend(iterable)` adds each element from an iterable. Both modify the list and return `None`.

```python
a = [1]
a.append([2, 3])           # [1, [2, 3]]
b = [1]
b.extend([2, 3])           # [1, 2, 3]
```

### Q13. How do `sort()` and `sorted()` differ?

`list.sort()` sorts a list in place and returns `None`. `sorted()` accepts an iterable and returns a new list. Both support `key` and `reverse`, and both are stable: equal-key elements keep their relative order.

```python
words = ["pear", "fig", "apple"]
ordered = sorted(words, key=len)  # ["fig", "pear", "apple"]
```

### Q14. What is the difference between assignment, shallow copy, and deep copy?

Assignment binds another name to the same object. A shallow copy creates a new outer container but shares nested objects. A deep copy recursively copies nested objects, subject to type-specific copying behavior.

```python
import copy

original = [[1], [2]]
alias = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0].append(99)
print(alias)              # [[1, 99], [2]]
print(shallow)            # [[1, 99], [2]]
print(deep)               # [[1], [2]]
```

### Q15. What are comprehensions?

Comprehensions build collections from iterables, optionally filtering elements. Prefer a normal loop when the expression becomes difficult to read.

```python
squares = [n * n for n in range(6) if n % 2 == 0]
lengths = {word: len(word) for word in ["cat", "python"]}
unique_lengths = {len(word) for word in ["cat", "dog", "python"]}
lazy_squares = (n * n for n in range(6))  # Generator expression.
```

### Q16. How can you remove duplicates while preserving order?

For hashable elements, use `list(dict.fromkeys(values))`. A set removes duplicates but does not promise the original order.

### Q17. Which collection operations should you know?

| Operation | Typical time complexity in CPython |
| --- | --- |
| List index access | O(1) |
| List append | O(1) amortized |
| List membership search | O(n) |
| List insertion/removal at the beginning | O(n) |
| Dictionary/set lookup | O(1) average; O(n) worst case |
| Sorting n elements | O(n log n) worst case |
| Copying a list of n elements | O(n) |

These assume ordinary element operations; custom comparison or hashing can add cost. Use `collections.deque` for efficient appends and removals at both ends.

### Q18. Why use `"".join(parts)` to build a string?

Strings are immutable. Joining many strings avoids relying on optimizations for repeated concatenation and clearly expresses the intent. Every element passed to `join()` must be a string.

```python
sentence = " ".join(["Learn", "Python", "daily"])
```

## 4. Control flow and functions

### Q19. How do `break`, `continue`, and loop `else` work?

`break` exits the nearest loop. `continue` skips to its next iteration. A loop's `else` runs when the loop finishes normally, including zero iterations, but not when it exits through `break`.

```python
for number in [1, 3, 5]:
    if number % 2 == 0:
        print("Found an even number")
        break
else:
    print("No even number found")
```

### Q20. What argument types can functions accept?

Functions support positional, keyword, default, variable positional (`*args`), and variable keyword (`**kwargs`) arguments. `/` marks positional-only parameters; parameters after `*` are keyword-only.

```python
def describe(name, /, greeting="Hello", *, uppercase=False):
    message = f"{greeting}, {name}"
    return message.upper() if uppercase else message

print(describe("Ada", uppercase=True))

def collect(*args, **kwargs):
    return args, kwargs    # args is a tuple; kwargs is a dict.
```

### Q21. Why are mutable default arguments dangerous?

Default values are evaluated when the function is defined, not on every call. A default list can therefore be shared across calls. Use `None` when a new collection is needed each time.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Q22. Does Python pass arguments by value or by reference?

Python passes object references by assignment, often called **call by sharing**. A parameter initially refers to the supplied object. Mutating that object can affect the caller; rebinding the parameter does not rebind the caller's name.

```python
def update(items):
    items.append(2)        # Mutates the caller's list.
    items = [99]          # Only rebinds the local name.

values = [1]
update(values)
print(values)             # [1, 2]
```

### Q23. What is LEGB scope?

For ordinary name lookup inside functions, Python searches **Local, Enclosing function, Global module, Built-in** scopes. Assignment normally makes a name local to the function.

- `global` lets a function rebind a module-level name.
- `nonlocal` lets a nested function rebind a name in an enclosing function scope.
- Reading a local variable before it has a value raises `UnboundLocalError`.

### Q24. What are first-class functions and closures?

Functions can be assigned to variables, passed as arguments, and returned from other functions. A closure retains access to variables from its enclosing function scope.

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
print(double(5))           # 10
```

### Q25. What is late binding in closures?

Closures look up captured variables when called. Functions created in a loop can therefore all observe the loop variable's final value. A default parameter can capture its value at each iteration.

```python
functions = [lambda: i for i in range(3)]
print([fn() for fn in functions])       # [2, 2, 2]

functions = [lambda i=i: i for i in range(3)]
print([fn() for fn in functions])       # [0, 1, 2]
```

### Q26. What is a decorator?

A decorator accepts a function or class and returns a replacement or modified object. Common uses include logging, caching, and access checks. `@decorator` above a function is essentially `function = decorator(function)`.

```python
from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@announce
def add(a, b):
    return a + b
```

`wraps()` preserves useful metadata such as the original name and docstring and exposes the wrapped function through `__wrapped__`.

### Q27. What is a lambda function?

A lambda is a small anonymous function containing a single expression. It follows ordinary function scope rules. Use `def` for multi-step logic or when a meaningful function name improves readability.

### Q28. What should you know about recursion?

A recursive function calls itself and needs a base case plus progress toward it. Python limits recursion depth and does not perform tail-call optimization. A loop or explicit stack is often better for very deep inputs.

## 5. Iterators and generators

### Q29. How do an iterable and an iterator differ?

An iterable can provide an iterator through `iter()`. An iterator provides successive values through `next()` and raises `StopIteration` when exhausted. An iterator's `__iter__()` returns itself.

```python
values = [10, 20]          # Iterable, not an iterator.
iterator = iter(values)
print(next(iterator))     # 10
print(next(iterator))     # 20
print(next(iterator, "done"))  # done
```

A list can supply fresh iterators. An exhausted generator does not automatically restart.

### Q30. What is a generator, and how does `yield` differ from `return`?

A function containing `yield` creates a generator when called. `yield` produces a value and suspends execution, preserving local state. `return` ends the function; in a generator, it ends iteration.

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print(list(countdown(3)))  # [3, 2, 1]
```

Generators produce values lazily, avoiding storage of every output at once. They can still retain substantial memory through their local variables or input references.

### Q31. What do `enumerate()` and `zip()` do?

`enumerate()` yields index-value pairs. `zip()` pairs elements from iterables and normally stops at the shortest input.

```python
for index, name in enumerate(["Ada", "Linus"], start=1):
    print(index, name)

pairs = list(zip(["a", "b"], [1, 2]))  # [("a", 1), ("b", 2)]
```

## 6. Object-oriented programming

### Q32. What are a class, an instance, and `self`?

A class defines behavior and attributes; an instance is an object created from that class. `self` conventionally names the instance parameter of an instance method. Python supplies it automatically when calling a bound method.

### Q33. How do instance attributes and class attributes differ?

Instance attributes belong to individual instances. Class attributes live on the class and are shared through attribute lookup unless shadowed. Shared mutable class attributes are a common bug.

```python
class Student:
    school = "Python Academy"       # Class attribute.

    def __init__(self, name):
        self.name = name             # Instance attribute.
        self.scores = []             # A new list per instance.
```

### Q34. How do instance, class, and static methods differ?

| Method | Implicit first argument | Typical use |
| --- | --- | --- |
| Instance method | `self`: instance | Operate on instance state |
| `@classmethod` | `cls`: class | Alternative constructors |
| `@staticmethod` | None | Related utility needing no instance/class state |

### Q35. What are inheritance, composition, and polymorphism?

- **Inheritance:** a subclass extends or specializes a base class; an “is-a” relationship.
- **Composition:** an object contains or delegates to another object; a “has-a” relationship.
- **Polymorphism:** different types support the same operation through a common interface.

Python often uses **duck typing**: code depends on supported behavior rather than a specific declared type. Prefer composition when there is no clear subtype relationship.

### Q36. What do MRO and `super()` mean?

The method resolution order determines the order Python searches classes for attributes. Inspect it with `ClassName.__mro__` or `ClassName.mro()`. `super()` delegates to the next class in that order, which is particularly important for cooperative multiple inheritance; it does not simply mean “call my parent.”

### Q37. How do `__new__()` and `__init__()` differ?

`__new__()` creates and returns an instance. `__init__()` initializes an instance after creation and must return `None`. Most classes only need to customize `__init__()`.

### Q38. What are special or dunder methods?

Special methods connect classes to Python syntax and built-in operations.

| Method | Purpose |
| --- | --- |
| `__repr__` | Developer-oriented representation |
| `__str__` | User-friendly string representation |
| `__len__` | Support `len(obj)` |
| `__eq__` | Define equality |
| `__iter__` / `__next__` | Support iteration |
| `__enter__` / `__exit__` | Support a context manager |
| `__call__` | Make an instance callable |

### Q39. Does Python have private attributes?

`_name` conventionally marks an attribute as non-public. `__name` inside a class triggers name mangling, primarily to avoid subclass naming collisions. Neither mechanism is a security boundary.

### Q40. What are properties and dataclasses?

`@property` exposes method logic through attribute access, useful for computed values or validation. `@dataclass` can generate methods such as `__init__`, `__repr__`, and `__eq__` for data-focused classes.

```python
from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)
```

`default_factory` creates a separate mutable default for each instance. Type annotations do not enforce types at runtime by themselves.

## 7. Exceptions, files, and project structure

### Q41. How do `try`, `except`, `else`, and `finally` work?

- `try` contains code that might raise an exception.
- `except` handles matching exceptions.
- `else` runs if the `try` block completes normally.
- `finally` runs as control leaves the construct, including during normal exception propagation or a return.

```python
try:
    number = int("42")
except ValueError as error:
    print(f"Invalid number: {error}")
else:
    print(number * 2)
finally:
    print("Conversion attempt finished")
```

Catch specific exceptions. Avoid returning from `finally`, because that can override a pending return or exception. Abrupt process termination can prevent cleanup from running.

### Q42. How do you raise and re-raise exceptions?

Use `raise ValueError("message")` for an invalid value. A bare `raise` inside an exception handler re-raises the active exception. `raise NewError(...) from error` explicitly chains exceptions. Custom application exceptions usually inherit from `Exception`.

### Q43. What is a context manager?

A context manager manages setup and cleanup around a `with` block using `__enter__()` and `__exit__()`. For files, it ensures closure when the block exits, including when an exception occurs.

```python
from pathlib import Path

path = Path("notes.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Python interview preparation\n")
```

You can also build context managers using `contextlib.contextmanager`.

### Q44. What are common file modes?

| Mode | Behavior |
| --- | --- |
| `r` | Read; file must exist |
| `w` | Write; create or truncate |
| `a` | Append; create if needed |
| `x` | Create exclusively; fail if already present |
| `b` | Binary mode modifier, for example `rb` |
| `+` | Enable reading and writing, for example `r+` |

Text mode works with `str` and an encoding. Binary mode works with `bytes`.

### Q45. What is the difference between a module and a package?

A module is an importable unit, commonly a `.py` file. A package organizes modules and subpackages. Regular packages typically contain `__init__.py`; namespace packages can omit it.

### Q46. Why use `if __name__ == "__main__":`?

When a module runs as the main program, its `__name__` is `"__main__"`. The guard allows script-specific code to run without executing it during an ordinary import.

```python
def main():
    print("Starting program")

if __name__ == "__main__":
    main()
```

### Q47. What are virtual environments and `pip`?

A virtual environment isolates a project's Python packages from other environments. `pip` installs packages; `python -m pip` runs it through the selected Python interpreter.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

`pip freeze` snapshots installed packages, including transitive dependencies; it is not a complete cross-platform lockfile strategy.

## 8. Advanced concepts and code quality

### Q48. How does Python manage memory?

CPython primarily uses reference counting, supplemented by a cyclic garbage collector. `del name` removes a binding; it does not guarantee immediate object destruction. Other references may keep the object alive, and other implementations can manage memory differently.

Use context managers for resource cleanup instead of depending on garbage collection timing.

### Q49. What is the GIL?

In conventional GIL-enabled CPython, the Global Interpreter Lock allows only one thread at a time to execute Python bytecode in an interpreter. Threads can still overlap I/O, and some native operations release the GIL.

The GIL does not make multi-step application logic thread-safe. Use synchronization for shared mutable state. Free-threaded CPython builds exist, so specify the interpreter and build when discussing GIL behavior.

### Q50. How do threading, multiprocessing, and `asyncio` differ?

| Approach | Common use | Key consideration |
| --- | --- | --- |
| Threading | Blocking I/O tasks | Shared memory; synchronization needed |
| Multiprocessing | CPU-heavy Python work | Separate processes; communication and startup overhead |
| `asyncio` | Many concurrent tasks with async I/O | Cooperative scheduling; blocking calls stall the event loop |

Concurrency means tasks can make overlapping progress. Parallelism means work executes simultaneously. `async def` defines a coroutine function; calling it creates a coroutine object whose execution must be awaited or scheduled.

### Q51. What are type hints?

Annotations describe expected types for readers, IDEs, and static type checkers. Python does not normally enforce them at runtime.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### Q52. How should you test and debug Python code?

Use small functions with clear inputs and outputs. Test ordinary cases, boundaries, empty inputs, invalid inputs, and expected exceptions. Python includes `unittest`, `breakpoint()`, and the `logging` module.

Use `assert` for internal invariants or tests, not required input validation: assertions can be disabled with optimization. Raise an explicit exception for validation that must always execute.

### Q53. What is caching, and when is it useful?

Caching stores previous results to avoid repeated work. `functools.lru_cache` can cache function calls with hashable arguments. It is useful for repeated computations but can retain objects in memory and produce stale results if external state changes.

### Q54. What are common Python code-quality principles?

- Follow consistent naming: `snake_case` for functions/variables and `PascalCase` for classes.
- Prefer clear code over clever one-liners.
- Avoid wildcard imports and names that shadow built-ins, such as `list` or `str`.
- Use `isinstance()` when subclass instances should be accepted.
- Avoid changing a collection's structure while iterating over it; build a new collection or iterate over a copy.
- Never use `eval()` or unpickle data from an untrusted source.

## 9. Common output and pitfall questions

### Q55. What does this nested-list example print?

```python
rows = [[0] * 2] * 3
rows[0][0] = 1
print(rows)               # [[1, 0], [1, 0], [1, 0]]
```

The outer repetition reuses the same inner list. Create independent rows with `[[0] * 2 for _ in range(3)]`.

### Q56. What does this mutable-default example print?

```python
def remember(value, seen=[]):
    seen.append(value)
    return seen

print(remember(1))        # [1]
print(remember(2))        # [1, 2]
```

Both calls use the same default list. Use the `None` pattern from Q21.

### Q57. Why does this print `None`?

```python
numbers = [3, 1, 2]
result = numbers.sort()
print(result)             # None
print(numbers)            # [1, 2, 3]
```

Many methods that mutate containers in place return `None`. Do not assign their result expecting the modified collection.

### Q58. Why is floating-point equality sometimes surprising?

Many decimal fractions cannot be represented exactly in binary floating point.

```python
import math

print(0.1 + 0.2 == 0.3)                 # False
print(math.isclose(0.1 + 0.2, 0.3))      # True
```

Choose tolerances appropriate to the problem, including an absolute tolerance when comparing values near zero. Use `decimal.Decimal` constructed from strings when decimal arithmetic is required.

## 10. Coding interview practice with solutions

State assumptions before coding, explain your approach, test edge cases, and discuss time and space complexity. The examples below assume ordinary hashing and comparison costs.

### Exercise 1. Check whether a string is a palindrome

Assumption: compare the original string exactly, including case, punctuation, and spaces.

```python
def is_palindrome(text):
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

assert is_palindrome("level")
assert is_palindrome("")
assert not is_palindrome("Python")
```

Time: O(n). Extra space: O(1). The shorter `text == text[::-1]` uses O(n) extra space for the reversed string.

### Exercise 2. Count character frequencies

```python
def frequencies(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

assert frequencies("banana") == {"b": 1, "a": 3, "n": 2}
assert frequencies("") == {}
```

Time: O(n) average. Extra space: O(k), where k is the number of distinct characters. Also know `collections.Counter(text)`.

### Exercise 3. Find the second-largest distinct integer

Return `None` when fewer than two distinct values exist. Avoid sorting to achieve a single pass.

```python
def second_largest(numbers):
    largest = second = None
    for number in numbers:
        if largest is None or number > largest:
            second, largest = largest, number
        elif number != largest and (second is None or number > second):
            second = number
    return second

assert second_largest([4, 1, 4, 3]) == 3
assert second_largest([-5, -2, -9]) == -5
assert second_largest([7, 7]) is None
assert second_largest([]) is None
```

Time: O(n). Extra space: O(1).

### Exercise 4. Check whether two strings are anagrams

Assumption: case and whitespace are significant.

```python
from collections import Counter

def are_anagrams(first, second):
    return Counter(first) == Counter(second)

assert are_anagrams("listen", "silent")
assert not are_anagrams("aab", "abb")
```

Time: O(n + m) average. Extra space: O(k) for distinct characters across both strings.

### Exercise 5. Find two indices whose values sum to a target

Return one matching pair, or `None` if no pair exists. A single element cannot be used twice.

```python
def two_sum(numbers, target):
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return seen[complement], index
        seen[number] = index
    return None

assert two_sum([2, 7, 11, 15], 9) == (0, 1)
assert two_sum([3, 3], 6) == (0, 1)
assert two_sum([3], 6) is None
```

Time: O(n) average. Extra space: O(n).

### Exercise 6. Validate balanced brackets

Assumption: ignore characters other than `()[]{}`.

```python
def balanced_brackets(text):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return not stack

assert balanced_brackets("a * (b + [c])")
assert not balanced_brackets("([)]")
assert not balanced_brackets("(")
```

Time: O(n). Extra space: O(n) worst case.

### More problems to practice independently

1. Find the first non-repeating character in a string.
2. Merge two sorted lists using two pointers.
3. Implement binary search and explain its sorted-input requirement.
4. Generate the first n Fibonacci numbers lazily.
5. Find missing and duplicate values under explicitly stated constraints.
6. Flatten one level of a nested list, then discuss arbitrary nesting.
7. Group words that are anagrams.
8. Implement a stack and a queue with suitable built-in containers.
9. Read a large text file one line at a time and count words.
10. Implement a timing decorator that preserves function metadata.

## 11. Final revision checklist

- [ ] Explain mutability, aliasing, equality, and identity with examples.
- [ ] Choose the right collection and explain its operation costs.
- [ ] Explain shallow/deep copies and shared mutable defaults.
- [ ] Use function arguments, LEGB scope, closures, and decorators.
- [ ] Distinguish iterables, iterators, and generators.
- [ ] Explain class/instance attributes, method types, MRO, and composition.
- [ ] Handle exceptions and files with appropriate cleanup.
- [ ] Explain modules, import guards, and virtual environments.
- [ ] Discuss the GIL with interpreter/build qualifications.
- [ ] Choose between threads, processes, and async I/O for a given workload.
- [ ] Solve coding exercises while stating assumptions and complexity.
- [ ] Test empty inputs, duplicates, negative numbers, and boundary cases.
