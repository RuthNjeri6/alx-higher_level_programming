# If Else Statements
```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
# For Statements 
Iterates over the items of any sequence (a list or a string) in the order that this items appear in the sequence  
```pthon
words = ['cat', 'window', 'car-wheel']
for w in words:
	print(w, len(w))
```
## output
```bash
cat 3
window 6
car-wheel 9
```

