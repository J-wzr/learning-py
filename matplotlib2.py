Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>>  #had stopped on subplots and to continue from here today
>>> # subplots help to plot two graphs on one figurre
>>> # the subplot function takes three args. the first arg is the representation of the rows and the second arg is the representation of columns while the third is the position of the subplot.
>>> #forexample
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.array([1,2,3,4,5,6])
>>> y = np.array([2,4,6,8,10,12])
>>> plt.subplot(1,2,1)
<AxesSubplot:>
>>> a = np.array([20,30,40,50,60])
>>> b = np.array([10,20,30,40,50])
>>> plt.subplot(1,2,2)
<AxesSubplot:>
>>> plt.show()
>>> # meaning that i can draw as many plots as i can using the subplot ment
>>> x = np.array([1,2,3,4,5,6])
>>> y = np.array([2,4,6,8,10,12])
>>> plt.title("first plot", loc="left", color="r")
Text(0.0, 1.0, 'first plot')
>>> plt.xlabel("fruits")
Text(0.5, 0, 'fruits')
>>> plt.ylabel("eaters")
Text(0, 0.5, 'eaters')
>>> plt.subplot(1,1,1)
<AxesSubplot:title={'left':'first plot'}, xlabel='fruits', ylabel='eaters'>
>>> plt.plot(x, y, marker="*", ms = "10", mec="r", mfc="b", ls=":", linewidth="0.5")
[<matplotlib.lines.Line2D object at 0x7fc6142e6e50>]
>>> a = np.array([20,30,40,50,60])
>>> b = np.array([10,20,30,40,50])
>>> plt.title("second figure")
Text(0.5, 1.0, 'second figure')
>>> plt.grid()
>>> plt.xlabel(""fishers)
SyntaxError: invalid syntax
>>> plt.xlabel(""fishers")
	   
SyntaxError: invalid syntax
>>> plt.xlabel("fishers")
Text(0.5, 0, 'fishers')
>>> plt.ylabel("salaries in'000's")
Text(0, 0.5, "salaries in'000's")
>>> plt.subplot(1,1,2)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#29>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 1289, in subplot
    key = SubplotSpec._from_subplot_args(fig, args)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/gridspec.py", line 608, in _from_subplot_args
    raise ValueError(
ValueError: num must be 1 <= num <= 1, not 2
>>> plt.subplot(1,1,3)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#30>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 1289, in subplot
    key = SubplotSpec._from_subplot_args(fig, args)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/gridspec.py", line 608, in _from_subplot_args
    raise ValueError(
ValueError: num must be 1 <= num <= 1, not 3
>>> plt.subplt(2,3,1)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#31>", line 1, in <module>
AttributeError: module 'matplotlib.pyplot' has no attribute 'subplt'
>>> plt.subplot(2,3,1)
<AxesSubplot:>
>>> plt.show()
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> #by doing all these errors give the overview of how deep you can rectify your mistakes and after knowing why, it becomes a walkover
>>> # what does that mean???? it means that if i am planning to draw many graphs, i should not restrict my graph values to one which will override the  properties  for the remaining graphs
>>> x = np.array([1,2,3,4,5,6])
>>> y = np.array([2,4,6,8,10,12])
>>> plt.subplot(2,2,1)
<AxesSubplot:>
>>> x = np.array([1,2,3,4,5,6])
>>> y = np.array([2,4,6,8,10,12])
>>> plt.title("first plot", loc="left", color="r")
Text(0.0, 1.0, 'first plot')
>>> plt.xlabel("fruits")
Text(0.5, 0, 'fruits')
>>> plt.ylabel("eaters")
Text(0, 0.5, 'eaters')
>>> plt.subplot(2,2,1)
<AxesSubplot:title={'left':'first plot'}, xlabel='fruits', ylabel='eaters'>
>>> a = np.array([20,30,40,50,60])
>>> b = np.array([10,20,30,40,50])
>>> plt.title("second plot", loc="left", color="r")
Text(0.0, 1.0, 'second plot')
>>> plt.plot(x, y, marker="*", ms = "10", mec="r", mfc="b", ls=":", linewidth="0.5")
[<matplotlib.lines.Line2D object at 0x7fc5fbdd1f70>]
>>> plt.plot(a, b, marker="+", ms = "10", mec="g", mfc="g", ls="--", linewidth="1.5")
[<matplotlib.lines.Line2D object at 0x7fc5fbddf2b0>]
>>> plt.subplot(2,2,2)
<AxesSubplot:>
>>> plt.show()
>>> # think got it now
>>> # matplotlib scatters
>>> 
>>> # lets start by plotting two scatterplots by replacing the word plot with scatter
>>> x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
>>> y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x7fc5fbd4e2e0>
>>> x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
>>> y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x7fc5fbd5a730>
>>> plt.show()
>>> # you can color each dot by adding the value of colors generated from the array of colors that we create ourselves
>>> # let me do it and i also add the colorbar() to show it
>>> x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
>>> y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
>>> colors = np.array([0,10,20,30,40,50,60,70,80,90,100])
>>> plt.scatter(x,y, c= colors, cmap="viridis")
Traceback (most recent call last):
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 4214, in _parse_scatter_color_args
    colors = mcolors.to_rgba_array(c)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/colors.py", line 377, in to_rgba_array
    rgba = np.array([to_rgba(cc) for cc in c])
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/colors.py", line 377, in <listcomp>
    rgba = np.array([to_rgba(cc) for cc in c])
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/colors.py", line 187, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/colors.py", line 269, in _to_rgba_no_colorcycle
    raise ValueError(f"Invalid RGBA argument: {orig_c!r}")
ValueError: Invalid RGBA argument: 0.0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#68>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2819, in scatter
    __ret = gca().scatter(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 4380, in scatter
    self._parse_scatter_color_args(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 4220, in _parse_scatter_color_args
    raise invalid_shape_exception(c.size, xsize) from err
ValueError: 'c' argument has 11 elements, which is inconsistent with 'x' and 'y' with size 13.
>>> colors = np.array([0,5,10,15,20,30,40,50,60,70,80,90,100])
>>> plt.scatter(x,y, c= colors, cmap="viridis")
<matplotlib.collections.PathCollection object at 0x7fc5fbcc0df0>
>>> plt.colorbar()
<matplotlib.colorbar.Colorbar object at 0x7fc5fbc24dc0>
>>> plt.show()
>>> # apart from viridis, there are other cmaps such as Accent, rainbow and others
>>> 
>>> 
>>> #now to bargraphs
>>> plt.bar(x,y)
<BarContainer object of 13 artists>
>>> plt.show()
>>> plt.barh(x,y)
<BarContainer object of 13 artists>
>>> plt.show()
>>> plt.bar(x,y,c="hotpink")
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#81>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2399, in bar
    return gca().bar(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 2403, in bar
    r.update(kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/artist.py", line 1064, in update
    raise AttributeError(f"{type(self).__name__!r} object "
AttributeError: 'Rectangle' object has no property 'c'
>>> plt.bar(x,y,color="hotpink")
<BarContainer object of 13 artists>
>>> plt.show()
>>> #note that if you wanna add width, it means that you're referring to the vertical bar graph and if you are talkin' about height, you're referring to the horizontal bar graph
>>> plt.barh(x,y, height= 0.5)
<BarContainer object of 13 artists>
>>> plt.show()
>>> #0.8 is default for both height and width
>>> plt.bar(x,y, width = 0.7)
<BarContainer object of 13 artists>
>>> plt.show()
>>> 
>>> #we're left with histograms and pie charts then the rest shall be covered in numpy as its also known as a good mathematical module for python
>>> #For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10
>>> np.random.normal(170, 10, 250)

>>> plt.(hist(x))
SyntaxError: invalid syntax
>>> plt.hist(x)
(array([2., 1., 2., 2., 3., 0., 2., 0., 0., 1.]), array([ 2. ,  3.5,  5. ,  6.5,  8. ,  9.5, 11. , 12.5, 14. , 15.5, 17. ]), <BarContainer object of 10 artists>)
>>> plt.show()
>>> #matplotlib piecharts
>>> plt.pie(x)
([<matplotlib.patches.Wedge object at 0x7fc5fbb1a9d0>, <matplotlib.patches.Wedge object at 0x7fc5fbb1aeb0>, <matplotlib.patches.Wedge object at 0x7fc5fbb2a3d0>, <matplotlib.patches.Wedge object at 0x7fc5fbb2a8b0>, <matplotlib.patches.Wedge object at 0x7fc5fbb2ad90>, <matplotlib.patches.Wedge object at 0x7fc5fbb362b0>, <matplotlib.patches.Wedge object at 0x7fc5fbb36790>, <matplotlib.patches.Wedge object at 0x7fc5fbb36c70>, <matplotlib.patches.Wedge object at 0x7fc5fbb44190>, <matplotlib.patches.Wedge object at 0x7fc5fbb44670>, <matplotlib.patches.Wedge object at 0x7fc5fbdf69a0>, <matplotlib.patches.Wedge object at 0x7fc5fba80040>, <matplotlib.patches.Wedge object at 0x7fc5fba80520>], [Text(1.0861827780782312, 0.17380153223218736, ''), Text(0.94378176310851, 0.5650451164498218, ''), Text(0.5799480371337046, 0.9346979588213314, ''), Text(0.08717498935686657, 1.0965402506203912, ''), Text(-0.22528728898701966, 1.076682700437264, ''), Text(-0.7961073980347128, 0.7590869586512468, ''), Text(-1.086182764856843, 0.17380161486000106, ''), Text(-1.0801215804258686, -0.20817629907922772, ''), Text(-0.9060442745987712, -0.623765799372478, ''), Text(-0.5194982342881994, -0.9695986719109321, ''), Text(0.2593347865995055, -1.0689927354567894, ''), Text(0.8646583907126143, -0.679974902014973, ''), Text(1.080121565807712, -0.20817637492543842, '')])
>>> plt.show()
>>> a = np.array([20,60,100,80])
>>> mylabels = np.array(["code","pro","net","is"])
>>> plt.pie(x, labels=mylabels)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#102>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2756, in pie
    return gca().pie(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 3058, in pie
    raise ValueError("'label' must be of length 'x'")
ValueError: 'label' must be of length 'x'
>>> plt.pie(a, labelx = mylabels)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#103>", line 1, in <module>
TypeError: pie() got an unexpected keyword argument 'labelx'
>>> plt.pie(a, labels = mylabels)
([<matplotlib.patches.Wedge object at 0x7fc5fbade250>, <matplotlib.patches.Wedge object at 0x7fc5fbade7c0>, <matplotlib.patches.Wedge object at 0x7fc5fbade3d0>, <matplotlib.patches.Wedge object at 0x7fc5fbaf4d60>], [Text(1.068035996798755, 0.26324724033138536, 'code'), Text(0.3900653535244525, 1.0285178753817767, 'pro'), Text(-1.0999999999999988, -5.149471622296949e-08, 'net'), Text(0.6248713159427525, -0.905282187227813, 'is')])
>>> plt.show()
>>> myexplode = np.array([0.2,0,0,0])
>>> plt.pie(x,explode=myexplode, shadow = True)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#107>", line 1, in <module>
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2756, in pie
    return gca().pie(
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "/home/josh/.local/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 3060, in pie
    raise ValueError("'explode' must be of length 'x'")
ValueError: 'explode' must be of length 'x'
>>> plt.pie(a,explode=myexplode, shadow = True)
([<matplotlib.patches.Wedge object at 0x7fc5fbe61af0>, <matplotlib.patches.Wedge object at 0x7fc5fbcc6040>, <matplotlib.patches.Wedge object at 0x7fc5fbcc6910>, <matplotlib.patches.Wedge object at 0x7fc6142f6190>], [Text(1.262224359853074, 0.3111103749370918, ''), Text(0.3900653535244525, 1.0285178753817767, ''), Text(-1.0999999999999988, -5.149471622296949e-08, ''), Text(0.6248713159427525, -0.905282187227813, '')])
>>> plt.show()
>>> plt.pie(a,explode=myexplode, shadow = True,startangle=90)
([<matplotlib.patches.Wedge object at 0x7fc61406eee0>, <matplotlib.patches.Wedge object at 0x7fc61406edc0>, <matplotlib.patches.Wedge object at 0x7fc5fbe39fd0>, <matplotlib.patches.Wedge object at 0x7fc5fbe399a0>], [Text(-0.3111103749370916, 1.262224359853074, ''), Text(-1.0285178753817765, 0.3900653535244527, ''), Text(5.149471664411206e-08, -1.0999999999999988, ''), Text(0.905282187227813, 0.6248713159427525, '')])
>>> plt.show()
>>> colors=["red","green","orange","black"]
>>> plt.legend()
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x7fc5fbcb20d0>
>>> plt.show()
>>> plt.pie(a,explode=myexplode, shadow = True,startangle=90)
([<matplotlib.patches.Wedge object at 0x7fc5fbbad8b0>, <matplotlib.patches.Wedge object at 0x7fc5fbbad6d0>, <matplotlib.patches.Wedge object at 0x7fc5fbd4eaf0>, <matplotlib.patches.Wedge object at 0x7fc5fbd4efa0>], [Text(-0.3111103749370916, 1.262224359853074, ''), Text(-1.0285178753817765, 0.3900653535244527, ''), Text(5.149471664411206e-08, -1.0999999999999988, ''), Text(0.905282187227813, 0.6248713159427525, '')])
>>> plt.show()
>>> y = np.array([35, 25, 25, 15])
>>> mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
>>> plt.pie(y, labels = mylabels)
([<matplotlib.patches.Wedge object at 0x7fc5fbd10d90>, <matplotlib.patches.Wedge object at 0x7fc5fbd242b0>, <matplotlib.patches.Wedge object at 0x7fc5fbd24790>, <matplotlib.patches.Wedge object at 0x7fc5fbd24c70>], [Text(0.4993895680663529, 0.9801071672559597, 'Apples'), Text(-1.086457168210212, 0.17207795223283895, 'Bananas'), Text(-0.172077952232839, -1.086457168210212, 'Cherries'), Text(0.9801071672559598, -0.4993895680663526, 'Dates')])
>>> plt.legend(title = "Four Fruits:")
<matplotlib.legend.Legend object at 0x7fc5fbbb62b0>
>>> plt.show()
>>> 
>>> 
>>> #bye ###josh wzr stack struggles
>>> ##seee you in numpy
>>> plt.show()
>>> 