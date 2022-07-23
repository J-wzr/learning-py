Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # modules are python dicts. just like the way you  pick a book from a shelf to go and use it is the way we gonna be importing python modules so that we are able to use them
>>> # to start with, is the python math module which we can import in a way like import math, same as from module import math *
>>> # but mostly we shall be saying from math import pi, sin, cos, acos etc to avoid that namespace which is large for each module in python
>>> 
>>> from math import pi, cos, sin, asin, exp, log
>>> x = math.cos((90/180)*math.pi)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#5>", line 1, in <module>
NameError: name 'math' is not defined
>>> import math
>>> from math import pi, cos, sin, asin, exp, log
>>> x = math.cos((90/180)*math.pi)
>>> print(x)
6.123233995736766e-17
>>> x = math.tan((45/180)*math.pi)
>>> print(x)
0.9999999999999999
>>> print(math.exp(2))
7.38905609893065
>>> print(math.log(2))
0.6931471805599453
>>> print(pow(2,3))
8
>>> # we didnt use the math method for pow coz pow is python inbuilt function
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> #dir to show all the available functions of  a certain module
>>> from math import floor, ceil, trunc
>>> print(ceil(0.3354))
1
>>> print(trunc(45.7344))
45
>>> print(floor(0.45))
0
>>> 
>>> from math import hypot, sqrt, factorial
>>> print(factorial(4))
24
>>> print(hypot(2,2))
2.8284271247461903
>>> print(sqrt(16))
4.0
>>> x = sqrt(16)
>>> print(trunc(x))
4
>>> #now to the random
>>> # computers work with the pseudo random numbers, not truly random numbers
>>> from random import random, seed
>>> seed(0)
>>> for i in range(5):
	print(random())

	
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085
>>> from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

SyntaxError: multiple statements found while compiling a single statement
>>> #the above will generate a random number  based on the specified conditions in the syntax when run one by one
>>> from random import randint
>>> for x in range(10):
	print(randint(1,10), end = " ")

	
7 5 8 6 10 4 9 3 5 3 
>>> # as you see, this is not a good solution to whenever you want to output a specific sequence of numbers
>>> #theres choice and sample
>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(choice(my_list))
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#48>", line 1, in <module>
NameError: name 'choice' is not defined
>>> from random import choice, sample
>>> print(choice(my_list))
2
>>> print(sample(my_list, 5))
[10, 5, 3, 8, 1]
>>> #the platform function
>>> #for it module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.
>>> from platform import platform
>>> print(platform)
<function platform at 0x7fe852ac03a0>
>>> print(platform())
Linux-5.15.0-41-generic-x86_64-with-glibc2.29
>>> print(platform(aliased = True, terse = True))
Linux-5.15.0-41-generic-x86_64-with-glibc2.29
>>> print(platform(aliased = False, terse = False))
Linux-5.15.0-41-generic-x86_64-with-glibc2.29
>>> #the platform parameters are used to show other relevant info that humans may need
>>> from platform import machine, processor
>>> print(processor(),machine())
x86_64 x86_64
>>> from platform import system
>>> print(system())
Linux
>>> from platform import version
>>> print(version())
#44~20.04.1-Ubuntu SMP Fri Jun 24 13:27:29 UTC 2022
>>> # also platform has a function to return the version of the python that am running
>>> #all in all, a module is a packet of functions and you can pack or add in as many functions as you want but theres one level than a module itself which is a package