# Data Structures: lambda, map, filter and reduce functions
## Introduction
This directory contain programs that demostarte the use of lambda, map, filter and reduce functions to manipulate the mutable data structures like lists and tuples:  
Below is a brief explaination of the various functions and concepts used in this directory.   
## Lambda
Lambda is used to define an anonymous function. if you dont want to give your function a name them use lambda to define it instead of ```def```   
### syntax
```python
lambda argument1, argument2: expression...
```
## Map()
Map function operate on each item of a list and returns a list  
## Filter()
Filter function also operate on a list or any othe mutable data structure and returns a list.   
For example:  
```python
a = [1, 2, 3]
print(list(filter((lambda x: x <=2), a)))
```
```bash
Output: 
[1, 2]
```
## Reduce()
Opreates on a list and return a single result not a list. 
