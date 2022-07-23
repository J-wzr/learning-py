# if, for and the while conditional statements
# starting with, is the if 
a, b, c, d, e = 12,3,-3,"hey", True
if a > b:
    print("indeed", a , "is greater than", b)



if a < b:
    print("indeed", a , "is greater than", b)
else:
    print("noo!", a , "is'nt less than", b)


if a < b:
    print("indeed", a , "is greater than", b)
elif a < 13:
    print("you were near to be chopped")
else:
    print("let's wait for next time")

#  so what was happening, if starts a condition, elif gives another condition if the first was not fulfilled and so on. Then else defines a block that will be executed if all conditions dint take place as they were supposed to take place
# there is a short hand if instead of writing the whole of that code
print("compressed function acted upon me") if a > b else print("i see")

# else if function with three conditions
print("it again acted up on me!") if a < b else print("confirmed not") if a == 12 else print("don't!")
# you can combine the if statements with the logical operators  and or 
# we can also do the  nested if statements

# doing the while loops,
i = 2
while i < 11:
    print(i)
    i += 2
# lets use while using the break and continue statements
i = 2
while i < 11:
    print(i)
    i +=1
    if i == 6:
        break
    
# control the behavior of the while loop otherwise, it gonna crush the browser and note that we use the continue before printing
i = 2
while i < 11:
    i +=1
    if i % 2 == 1:
        continue
    print(i)
    
# now using the for loop can enable us loop through big iterables
string, lst, tupl = "apple", ["tomatoes", "cherry"], ("man", 123)
for x in string:
    print(x)

for x in lst:
    print(x)
    if "tomatoes" in lst:
        break

for x in range(99,151):
    if x % 2 != 0:
        continue
    print(x)

# nested for loop
