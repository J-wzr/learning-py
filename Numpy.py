Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> """NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python."""
'NumPy is a Python library used for working with arrays.\n\nIt also has functions for working in domain of linear algebra, fourier transform, and matrices.\n\nNumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.\n\nNumPy stands for Numerical Python.'
>>> import numpy as np
>>> print(numpy.__version__)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#2>", line 1, in <module>
NameError: name 'numpy' is not defined
>>> # it can be seen that it can't be found since  i earlier aliased the numpy
>>> print(np.__version__)
1.23.1
>>> arr = np.array([1,2,3,4,5,6])
>>> print(arr)
[1 2 3 4 5 6]
>>> print(type(arr))
<class 'numpy.ndarray'>
>>> # you can see that python  tells us that the type above is an ndarray so to create anything as an ndarray, normalize passing it in the array as aparameter
>>> arr = np.array((2,3,4,5,6,7))
>>> print(arr)
[2 3 4 5 6 7]
>>> # dimensions in arrays
>>> # a zero dimension array is the one we're dealing with. but higher dimension arrays are there such as a 2d and a 3d arra just by increasing the number of brackets being given to it as that array
>>> arr = np.array([[1,2,3],[4,5,6]])
>>> print(arr.ndim)
2
>>> # ndim checks the number of dimensions that are contained in thar array
>>> arr = np.array([[[1,2],[3,4]],[[1.2,.3,.4],[.5,.6,.7]]])

Warning (from warnings module):
  File "<pyshell#16>", line 1
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
>>> arr = np.array([[[1,2],[3,4]],[[1.2,.3,.4],[.5,.6,.7]]])
>>> print(arr.ndim)
2
>>> # a 3d array is not that easy to create
>>> arr = np.array([[[1,2],[3,4]],[[.1,.2],[.3,.4]]])
>>> print(arr.ndim)
3
>>> # for higher dimensions like five, we're going to be using the specification ndmin=5 and so on, like in the example below
>>> arr = np.array([1,2,3,4,5,6], ndmin = 5)
>>> print(arr)
[[[[[1 2 3 4 5 6]]]]]
>>> print(arr.ndim)
5
>>> #array indexing
>>> arr = np.array([1,2,3,4,5])
>>> print(arr[0])
1
>>> print(arr[3]+arr[5])
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#29>", line 1, in <module>
IndexError: index 5 is out of bounds for axis 0 with size 5
>>> print(arr[3]+arr[4])
9
>>> arr = np.array([[1,3,2],[4,5,6]])
>>> print(arr[1,1])
5
>>> # the first para shows the row dimension and the second para shows the  column dimension and that is how i aimed at accessing the contents of the 2d array elements
>>> # accessing the third element of the second array, of the first array given the array below
>>> arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

>>> print(arr[0,1,2])
6
>>> # we can also do negative indexing given the position of the array elements is studied so well
>>> # now to array slicing
>>> 
>>> arr = np.array([1,2,3,4,5])
>>> print(arr[1:3])
[2 3]
>>> # that's the start: end method and we can also use the start:end:step method to access our values but while we're  skipping some
>>> arr = np.array([1,2,3,4,5,6,7,8,9])
>>> print(arr[1:8:2])
[2 4 6 8]
>>> # also do negative slicing which is easy at the same time
>>> # slicing 2d arrays
>>> # say, from the second element, slice elements from index 1 to index 4
>>> arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
>>> print(arr[1,1:4])
[7 8 9]
>>> # brings one array apart from if we were  given to slice from both elements
>>> print(arr[0:2,1:4])
[[2 3 4]
 [7 8 9]]
>>> print(arr[0:2,2])
[3 8]
>>> 
>>> 
>>> # bra bra braa now numpy dtype
>>> print(arr.dtype)
int64
>>> # take note that its not the same as type coz by now, i've only seen numpy with one type of its objects i.e ndarrays
>>> # but for whatever will be inside that array, it will be constituting its own dtype
>>> arr = np.array((1,2,3))
>>> print(arr.dtype)
int64
>>> arr = np.array(['apple', 'banana', 'cherry'])
>>> print(arr.dtype)
<U6
>>> # by fact, we can create arrays with defined data types by passing it in an array as  a parameter
>>> arr = np.array(['banana', 23, "cherry", dtype = 'b'])
SyntaxError: invalid syntax
>>> arr = np.array(['banana', 23, "cherry"], dtype = 'b')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#65>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'banana'
>>> arr = np.array(['banana', 23, "cherry"], dtype = 'S')
>>> print(arr.dtype)
|S6
>>> # copying arrays can be done with either copy or view but view brings a copy of a new array while copy overrides the original array rules by extracting all original array elements and bringing them to a new array
>>> # if you are not sure of the array that you're dealing with, you can maybe first check if it owns its own data or not
>>> arr = np.array([1,2,3,4,5])
>>> x = arr.view()
>>> y = arr.copy()
>>> print(x.base)
[1 2 3 4 5]
>>> print(y.base)
None
>>> 
>>> # numpy array reshape
>>> #return the shape of an array
>>> print(x.shape)
(5,)
>>> # means that its a 1d array where the element has 5 members
>>> examplearray = np.array([[[1,3],[3,4]],[[.1,.3],[.3,.4]]])
>>> print(examplearray.shape)
(2, 2, 2)
>>> # got it
>>> #reshaping means changing the shape of an array element
>>> #reshaping from 1d to 2d
>>> arr = np.array([1,2,3,4,5,6])
>>> arr.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
>>> # the first figure represents array number and the last figure represents number of elements to be in that array
>>> # reshaping from 1d to 3d
>>> arr = np.array([1,2,3,4,5,6])
>>> arr.reshape(2,2,1)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#90>", line 1, in <module>
ValueError: cannot reshape array of size 6 into shape (2,2,1)
>>> arr.reshape(2,1,2)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#91>", line 1, in <module>
ValueError: cannot reshape array of size 6 into shape (2,1,2)
>>> # all
>>> 
>>> 
>>> #all in all, knowing the formular and being organized will create a good result
>>> # but a successful reshaping goes hand in hand with a plan of how many elements are contained in your array, plus knowledge about unknown dimension
>>> 
>>> #flattening arrays is also possible incase you wanna convert them back to 1d
>>> examplearray.reshape(-1)
array([1. , 3. , 3. , 4. , 0.1, 0.3, 0.3, 0.4])
>>> 
>>> 
>>> # Numpy array iterating
>>> for x in examplearray:
	print(x)

	
[[1. 3.]
 [3. 4.]]
[[0.1 0.3]
 [0.3 0.4]]
>>> arr = np.array([[1, 2, 3], [4, 5, 6]])

>>> for x in arr:
	for y in x:
		print(y)

		
1
2
3
4
5
6
>>> # what does that indicate? it means that if we iterate on an nd array, it will go through the elements of the array n-1 times
>>> # meaning for 2d, we have 2 for statements and for 6d, we have 6 for statements
