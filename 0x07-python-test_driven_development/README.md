# Test Driven Development 
This directory focuses on the use of doctest to test python modules, classes, methods and functions.  
All the tests are documented externally on txt files located in the tests folder. 
To test the various modules:
1. Clone this repository
2. Navigate to the ```0x07-python-test_driven_development``` folder
3. Create a virtual environment and activate it
   ```bash 
   python3 -m venv env-test  
   source env-test/bin/activate
   ```
4. Run the files located in the mains folder by running the following command:
   ```bash
   python3 mains/filename.py
   ```
5. Run the tests file related to the module 
   ```bash
   python3 -m doctest -v ./tests/filename.txt
   ```
   
Below is a brief explanation of the doctest module, its options and how to use it: 

## The doctest module
This module searches for interactive python sessions and executes them to check if they work as shown.  

## Testing through Documentation
When the doctest is called it searches for lines beginning with (>>>) i.e interpreter prompt, thats where the test case begins.  
The test case ends with a new line or by the next interpreter prompt. eg

```python

# doctest_simple.py
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
```

### Handling unpredicted output

When the tests include values that are bond to change, and the value is not important and can be ignored, then ELLIPSIS option(...) is used to ignore the verification value.

```python
# doctest_ellipsis.py
class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]
```

For value that cannot be ignored, e.g keys of dictionary or indices of sets, the solution would be to look for specific keys individually, generating a sorted list of the contents of the data structure or comparing against a literal value for equality instead of depending on the string representation.

### Tracebacks
Tracebacks do change because it depends with the location, which changes. 
doctest makes effort to recognize tracebacks and ignore the parts that might change from system to system.

```python
# doctest_tracebacks_no_body.py
def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
```

### Working around whitespace
Use the option NORMALIZE_WHITESPACE for any whitespace on the expected value to match the whitespace on the output. 
For new lines add <BLANKLINE> where you need the output to have a new line otherwise newlines are interpreted as end of test case

```python
# doctest_blankline.py
def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()
```

### Test locations
test are located on the module, class, method and function level. 
At times test are included on the module as dictionary of variable name __test__ with values specifying the location of other tests.   

### External documentation 
Having test on the same file as your code is not the pythonic way, instead have all the tests in a .txt file. The following is an example:

```
# doctest_in_help.txt
===============================
 How to Use doctest_in_help.py
===============================

This library is very simple, since it only has one function called
``my_function()``.

Numbers
=======

``my_function()`` returns the product of its arguments.  For numbers,
that value is equivalent to using the ``*`` operator.

::

    >>> from doctest_in_help import my_function
    >>> my_function(2, 3)
    6

It also works with floating-point values.

::

    >>> my_function(2.0, 3)
    6.0

Non-Numbers
===========

Because ``*`` is also defined on data types other than numbers,
``my_function()`` works just as well if one of the arguments is a
string, a list, or a tuple.

::

    >>> my_function('a', 3)
    'aaa'

    >>> my_function(['A', 'B', 'C'], 2)
    ['A', 'B', 'C', 'A', 'B', 'C']

```

### Running test
Command line method:
```bash 
python3 -m doctest -v doctest_someFile.py
```

Command line method of running test is not ideal when the tests are in different files. Instead there are other ways to run tests including:
#### By Module 
Add instructions to run the test at the bottom of the modules. calls the testmod() function of the doctest module
```python
# doctest_testmod.py
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```
#### By File
Same as by module but uses the testfile() function of the doctest module
```python
# doctest_testfile.py
import doctest

if __name__ == '__main__':
    doctest.testfile('doctest_in_help.txt')
```

### Unittest suite
When both the unittest and doctest are used for testing the same code in different situations, the unittest integration in doctest can be used to run tests together. 
The classes DocTestSuite and DocFileSuite create test suites compatible with test-runner API of unittest.
### Test context
The execution context created by doctest as it runs tests contains a copy of module-level globals for the test module. Each test source (functions, class module) has its own set of globals to isolate the tests from each other. so its less likely to interfere with one another.

even so, if mutable variables are changed there is interference t avoid this global variables can be passed to testmod() and testfile() to have the context set up using data controlled by the caller.