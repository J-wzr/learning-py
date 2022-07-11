#summary of it in small portions of data types, variables, and basic operators
#all other beginners steps skipped
#starting from variable names which you can assign like three in one line
x, y, z, a, b = 20, " sEcond", True, "first", 30
print(y)
'''you can output multiple variables at once''' 
print(z, y, x) # just coz a comma creates its own space, it may not need your space inside the print function
#or concatenate them if they are all strings but not strings and numbers or other categories
print(a +" " + y) 
print(x + b)
print("hey\nBro\nI love\nyou") #this is called the escape character to start new lines
#here comes the implicit use of the keyword args such as the end and the sep keywords
print("This string is concatinated using the end keyword to connect it to the", end=" ")
print("next print function")
#change the behaviour of python that directly applies spaces as separators
print("python", "is", "interesting", sep="-", end=" ")
print("next","damn","you","see", 'the'," print function", sep=" ***" )
#another confirmed xter that can escape the quotes is the escape char \ as the example below but there are other xters like b, r, ooo nd xxh
print("\"\"\"I'm\"\"\"")

#data types inbuilt in python text are str, numerics are int float and complex, etc as we are going to see through out the workarounds
#to display a data type, just use the type constructor
print(type(x)) #  will print its class as int since i grobally created it before

#python numbers, strings, and their methods
print(2 * 3, 2 * 2, 2. * 2, 6 / 3, 6/3.5, 6//3.5, sep="\n and also got this: ") #the // works for float values and returns a value with a .0
print(y[-4:-1]) #make sure this is left side binded in that the starting integer is plainly greater than the right
print(y.upper(), y.lower(), y.strip(), y.replace("s","j"))
#we saw that strings can't be concatenated with numbers but the format method came to save us
txt="I am called {0} and I have {1} years old"
name = "Josh"
age = 38
print(txt.format(name,age))
#but to note, there are many string methods that can just be exhausted incase you concentrate on them
#you can check if sth is a string or not
print(isinstance(y, str)) #this gonna bring you a boolean string that you want

