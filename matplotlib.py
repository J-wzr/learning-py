Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # looking at matplotlib in python
>>> import matplotlib
>>> #for checking the version of it
>>> print(matplotlib.__version__)
3.5.2
>>> #the main function that lies under matplotlib is pyplot
>>> import matplotlib.pyplot as plt
>>> #then now since we're going to access the mathematical part of python, also import numpy as np
>>> import numpy as np
>>> xpoints = [1,3,4,5,6,7,8]
>>> ypoints = [20,30,40,50,60,70,80]
>>> #but if you let them to be like that, you wont be successful in that you have to generate it inform of an array which fortunately python has as one of its inbuilt functions
>>> xpoints = np.array[1,2,3,4,5]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#11>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> xpoints =np.array([1,2,3,4,5])
>>> ypoints =np.array([20,30,40,50,60])
>>> plt.plot(xpoints,ypoints)
[<matplotlib.lines.Line2D object at 0x7fd6949991c0>]
>>> plt.show()
>>> #so now i have completed drawing a simple line graph
>>> #if you leave out some points, they are neglected and by default, python generates its own points from 0, onwards according to how your graph values are many
>>> #
>>> #now to the markers
>>> 
>>> plt.plot(xpoints,ypoints, marker = '*', ms = '20', mec = 'hotpink', mec = 'hotpink')
SyntaxError: keyword argument repeated
>>> #oh! sorry but for markers, just marker has many formats in which it can be expressed such as *, +, Y, o, e.t.c and ms is its size and mec is its outer color then mfc is its inner color
>>> plt.plot(xpoints,ypoints, marker = '*', ms = '20', mec = 'hotpink', mfc = 'hotpink')
[<matplotlib.lines.Line2D object at 0x7fd6946f7340>]
>>> plt.show()
>>> 
>>> 
>>> #now to the line
>>> #we have ls, we have c and we have linewidth where the ls, linestyle can be expressed in its known shortened codes of :, -., --, e.t.c
>>> a = np.array([2,4,6,8,10])
>>> b = np.array([10,5,15,10,20])
>>> plt.plot(a,b,xpoints, marker = 'o', ms = '10',c='b',linewidth = '10',ls = '"')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#31>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2769, in plot
    return gca().plot(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 1632, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_base.py", line 312, in __call__
    yield from self._plot_args(this, kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_base.py", line 538, in _plot_args
    return [l[0] for l in result]
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_base.py", line 538, in <listcomp>
    return [l[0] for l in result]
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_base.py", line 531, in <genexpr>
    result = (make_artist(x[:, j % ncx], y[:, j % ncy], kw,
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_base.py", line 351, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/lines.py", line 366, in __init__
    self.set_linestyle(linestyle)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/lines.py", line 1122, in set_linestyle
    _api.check_in_list([*self._lineStyles, *ls_mapper_r], ls=ls)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/_api/__init__.py", line 129, in check_in_list
    raise ValueError(msg)
ValueError: '"' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
>>> plt.plot(a,b,xpoints, marker = 'o', ms = '10',c='b',linewidth = '10',ls =':')
[<matplotlib.lines.Line2D object at 0x7fd694679040>, <matplotlib.lines.Line2D object at 0x7fd694679100>]
>>> plt.show()
>>> clear
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#34>", line 1, in <module>
NameError: name 'clear' is not defined
>>> #qn. print three lines and by default, see if they can decide to have different colors
>>> x1 = np.array([0, 1, 2, 3])
>>> y1 = np.array([3, 8, 1, 10])
>>> x2 = np.array([0, 1, 2, 3])
>>> y2 = np.array([6, 2, 7, 11])
>>> plt.plot(x1, y1, x2, y2)
[<matplotlib.lines.Line2D object at 0x7fd6946158b0>, <matplotlib.lines.Line2D object at 0x7fd694615910>]
>>> plt.show()
>>> 
>>> 
>>> #pyplot labels
>>> #python got us the xlabel, the ylabel and the title by using its matplotlib module and we gonna make use of it even to add styles to the titles
>>> plt.xlabel("poverty levels")
Text(0.5, 0, 'poverty levels')
>>> plt.ylabel("difference")
Text(0, 0.5, 'difference')
>>> plt.title("Economic differences in Uganda")
Text(0.5, 1.0, 'Economic differences in Uganda')
>>> plt.show()
>>> font1 = {'family':'serif','color':'blue','size':20}
>>> font2 = {'family':'serif','color':'darkred','size':15}
>>> a = np.array([1,1.5,2,2.5,3,3.5])
>>> b = np.array([2,4,6,8,10,12])
>>> plt.xlabel("sugar", fontdict = font1)
Text(0.5, 0, 'sugar')
>>> plt.ylabel("price", fontdict = font2)
Text(0, 0.5, 'price')
>>> plt.title("Sugar against price")
Text(0.5, 1.0, 'Sugar against price')
>>> plt.show()
>>> plt.plot(a,b)
[<matplotlib.lines.Line2D object at 0x7fd694525640>]
>>> plt.show()
>>> #you can use loc = left, center, or right to specify the location of the title for the graph  you're drawing
>>> #now grid editting as follows
>>> 
>>> 
>>> #the grid refers to the lines that are behind the graph
>>> #when you just say plt.grid(), only what occurs are both the  x and y grid lines yet sometimes you might want to plot only the x grid lines so just add the  plt.grid(axis = "x")
>>> plt.show()
>>>  a = np.array([1,1.5,2,2.5,3,3.5])
 
SyntaxError: unexpected indent
>>> a = np.array([1,1.5,2,2.5,3,3.5])
>>> b = np.array([2,4,6,8,10,12])
>>> font1 = {'family':'serif','color':'blue','size':20}
>>> font2 = {'family':'serif','color':'darkred','size':15}
>>> plt.plot(a,b, marker = "o", ms = 15, mec = "r", ls = '-')
[<matplotlib.lines.Line2D object at 0x7fd6942889a0>]
>>> plt.grid()
>>> plt.title("A fine plotting")
Text(0.5, 1.0, 'A fine plotting')
>>> plt.xlabel("hiiii",fontdict = font1)
Text(0.5, 0, 'hiiii')
>>> plt.ylabel("hahhhh", fontdict = font2)
Text(0, 0.5, 'hahhhh')
>>> plt.show()
>>> 
>>> #so, with matplotlib, we can easily draw graphs of different stles and of any mathematics and save the graphs
>>> #remember we can also give the gridlines the color, linestyle and the color width
>>> 
>>> #now to matplotlib sub plots
>>> #😎️🤣️

