Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # while in sql we joij arrays using the keys, in python numpy we join arrays considering their axes. if the axis is not specified, it turns out to be
>>> arr1 = np.array([1,2,3,4])
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
NameError: name 'np' is not defined
>>> import numpy as np
>>> arr1 = np.array([1,2,3,4])
>>> arr2 = np.array([5,6,7])
>>> newarr = arr1.concatenate(arr2)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#5>", line 1, in <module>
AttributeError: 'numpy.ndarray' object has no attribute 'concatenate'
>>> newarr = np.concatenate((arr1),(arr2))
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#6>", line 1, in <module>
  File "<__array_function__ internals>", line 180, in concatenate
TypeError: only integer scalar arrays can be converted to a scalar index
>>> newarr = np.concatenate((arr1,arr2))
>>> print(newarr)
[1 2 3 4 5 6 7]
>>> #oh finally out of that stackloop
>>> # join two 2d arrays with axis equal to one
>>> #joining using stacks
>>> #just use np.stack((arr1,arr2,...)) and joining along rows, just say np.hstack and along columns, just use np.vstack and finally along height(which is usually known as depth,) use np.dstack((arrs))
>>> 
>>> #array split arrays
>>> arr = np.array_split(newarr,2)
>>> print(arr)
[array([1, 2, 3, 4]), array([5, 6, 7])]
>>> # we can also access split arrays the usual way we access array elements
>>> # like stack functions, we can split along rows and along columns whatever dimension the array is in
>>> 
>>> #array search
>>> # using the where() method and it returns the index
>>> # maybe np.searchsorted which may be somewhat complex as it shows where a specific xter should be placed to match the given array
>>> np.searchsorted(arr, 7,side="right")

Warning (from warnings module):
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 43
    result = getattr(asarray(obj), method)(*args, **kwds)
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#23>", line 1, in <module>
  File "<__array_function__ internals>", line 180, in searchsorted
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 1387, in searchsorted
    return _wrapfunc(a, 'searchsorted', v, side=side, sorter=sorter)
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 54, in _wrapfunc
    return _wrapit(obj, method, *args, **kwds)
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 43, in _wrapit
    result = getattr(asarray(obj), method)(*args, **kwds)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> ##sorting arrays
>>> np.sort(arr)

Warning (from warnings module):
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 1003
    a = asanyarray(a).copy(order="K")
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#25>", line 1, in <module>
  File "<__array_function__ internals>", line 180, in sort
  File "/home/josh/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py", line 1004, in sort
    a.sort(axis=axis, kind=kind, order=order)
ValueError: operands could not be broadcast together with shapes (3,) (4,) 
>>> arr = np.array([1,3,2,4,5,33])
>>> print(np.sort(arr))
[ 1  2  3  4  5 33]
>>> ##filtering arrays
>>> ##we filter arrays using a boolean index lists
>>> ## we meet in python random
>>> 