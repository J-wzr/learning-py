#lists, tuples, sets and dictionaries
my_list = [1,2,"word",True, ("me", "ben", "tupp"),{"fname":"John","sname":"Doctor"}]
mylist = list((True, "John"))
print(mylist)
print(mylist[1]) #you can also access items while slicing like as seen beffore in strings
print(type(my_list))
print(my_list[4:7])
print(my_list[-3:-1])
#slicing in this case mastered
#i want to check if the item exists in the list created by using the if statement that will be exhausted later in this workarounds
if False not in my_list:
	print("yes bro it exists")
else:
	print("nat!!!!")
#those were manipulated many times and  you can also do the same
# add items to the list or change them in these ways
my_list[1] = 3
print(my_list)
my_list.insert(2,"another word")
print(my_list)
my_list.append("appended item")
print(my_list)
mytuple = ("mytupleItem",)
mylist.extend(mytuple)
print(mylist)   #you can extend any iterable item to the list item, not specifically a list
#you can remove pop delete clear and delete list items or all list
my_list.remove(1)
print(my_list)
my_list.pop(-1)
print(my_list)
del my_list[-1]
print(my_list)
# my_list.clear()
# print(my_list)
# clears the whole list
# del my_list
# print(my_list) deletes the whole list

# looping through lists
for x in my_list:
	print(x)
#you can also use the index numbers using the for loop
for i in range(len(my_list)):
	print(my_list[i])
#you can also loop through the list using the while loop but specify the starting and the increment operators coz if not you'll get stuck in aloop
i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
#list comprehension big subtopic
[print(x) for x in my_list]
#first create a new list with values basing on the existing ones and later convert everything you coded in alist comprehension
my_word_list = ["word", "ewe", "crocodile"]
newlist =[]
for x in my_word_list:
	if "w" in x:
		newlist.append(x)
print(newlist)
#could be written like the comprehended list below
newlist = [x for x in my_word_list if "w" in x]
print(newlist)
#use the ranges and after convert them to accept the rules
for x in range(10):
	print(x)
[print(x) for x in range(10, 21)] #this is what they call a list comprehension
# sorting lists
my_word_list.sort(reverse = True)
print(my_word_list)
# for ascending order, its set by default en no need of reversed
#the arg key = str.lower is used incase the string is a mixture of the lower and uppercase letters coz by default, it sorts uppercase before lower case letters
my_word_list.sort(reverse = True, key = str.lower)
print(my_word_list)
#copying lists
#just say newlist = list1.copy()     or say newlist = list(list1)

#we're now gonna join lists 
newlist1 = my_list + mylist
print(newlist1) 
#or you can also use the for loop to join the lists
for x in my_list:
	mylist.append(x)

print(mylist)

#you can also use the extend method to join lists

#if theres anything left, not to be hesitant to add it there
usersname = str(input("let me know your name please: "))
print(usersname)
print("oh! JoshWzr is glad to know you dear", usersname)
input("so how did you find this summary? ")
print("okay, i see")


# python tuples are ordered, unchangeable and can contain  duplicate values
my_tuple1 = ("apples","tomatoes", "cherry")
print(type(my_tuple1))
my_tuple2 = tuple(("camel", "cow" , "goats", "hoarse"))
print(len(my_tuple2))
# accessing the tuple items is the same as accessing items with the indexes and by now this is easy for us
# even the slicing is the same
print(my_tuple1[-2:-1])
# tuple items are immutable but theres a way you can use to fix that issue 
# one by first changing it to a tuple, then thereafter, add your items and change it back to a tuple
# second, you can add a tuple into a tuple
changed = list(my_tuple2)
changed.append("added")
changed_tuple = tuple(changed)
print(changed_tuple)
# that was the first method and the second method is the one below
y = ("insideTuple",)
changed_tuple += y
print(changed_tuple)
# now unpacking tuples means assigning the tuple results to variables
a,b,c = my_tuple1
print(a,b,c, sep="***")
# let say they were many elements in a tuple and you wanted to assign the ones left with the same value, use the asterisk *
d,e,*f = my_tuple2
print(d,e,f, sep="*+")

# loop through tuples
[print(x) for x in my_tuple1 if "apples" in my_tuple1]
# in the example above, i used the compressed functions
[print("wooo") for x in range(len(my_tuple1))]
# then we're goin to loop through the tuple using the while loop
i = 0
while i<len(my_tuple2):
	print(my_tuple2[i])
	i+=1
# joining tuples
joined_tuple = my_tuple1 + my_tuple2
print(joined_tuple)
# or by multiplying them,,
print(joined_tuple * 3)
# tuple two methods it 
print(my_tuple2.count("cow"))
print(my_tuple2.index("cow"))
 

# sets in detail
my_set = {"fish", 1, 2, "meet", 484, ("expect", "shmurda"), True}
# unordered, unchangeable and are un indexed 
# use name, use type like in other items]
# now the qn comes how do we access them
#u can maybe loop through the set to access its contents or ask if a certain element does exist in a set by using the in keyword

for x in my_set:
	print(x)
# to be surprised, sets have completely different methods from other iterables in such way below
my_set.add("addedItem")
print(my_set)
# adding items from another set to the current set but note that we cannot update an empty set as python may call it an empty dictionary
my_set1 = {"toAdd"}
my_set1.update(my_set)
print(my_set1)
# remember its not only the other dictionaries that we add there into  a dictionary but we can update it with all other iteraables
# remove or discard an item removes elements of a set
my_set.remove(True)
print(my_set)
# removing an element that does not exist will raise an error but using discard will not raise an error
my_set.discard(774)
print(my_set)

# using a for loop method loops well through a set 
set1 = {2,3,3443,"gjeri"}
set3 = my_set.union(set1)
print(set3)
# the intersection update method will output the items that are in both sets but the intersection only brings a new set containing only the intersection items
# the sets also have the symmetric_difference_update that returns all but not different items 
# sets are iterable objects that have very many methods that can't  be exhausted en it has many methods more compared to other iterable items

# python dictionaries explanations
dict1 = {"fname":"josh", "lname":"wzr", "nick_name":"Mwesigwa", "friends":("henessy", "benit")}
print(type(dict1))
# they are ordered, changeable but don't allow duplicate items
print(dict1["friends"])
get = dict1.get("fname")
print(get)
# we can change the items and access the keys only , we can update a dictionary key to another name
dict1['age'] = '100years'
key = dict1.keys()
print(key)
vals = dict1.values()
print(vals)
# the items function will output all items in a dictionary as tuple elements
print(dict1.items())
# we can delete, pop, popitem or clear or delete the whole dictionary
dict1.popitem()
print(dict1)
dict1.pop("fname")
print(dict1)
del dict1["lname"]
print(dict1)
dict1.clear()
print(dict1)
del dict1
# print(dict1) removes the whole dict
# loop through dictionaries
dict2 = {"fname":"josh", "lname":"wzr", "nick_name":"Mwesigwa", "friends":("henessy", "benit")}
# remember we have keys and values in our dictionaries
for x in dict2:
	print(x)

# this will do a repeat on keys only
for x in dict2.values():
	print(x)
for x in dict2.keys():
	print(x)
for x in dict2:
	print(dict2[x])
for x,y in dict2.items():
	print(x,y)


anotherdict = dict2.copy()
print(anotherdict)
# there above, we copied that dictionary
# but we can use the dict constructor property
# dictionaries can also be nested

# dictionary methods
# they also have the clear, the copy and other various methods 
