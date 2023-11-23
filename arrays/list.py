a = [1,"atharv",True,False,2]

#accesssing list items
print(a[1])
print(a[:2]) # return array of items till index 2 . index 2 not included
print(a[2:]) # return array of items from index 2 . index 2 included
print(a[1:3]) # return array of items from index 1 to 3 . index 1 included , index 3 not included

#change list items
a[1] = 2
a[1:3] = [10,20,30]
print(a)

#add items
a.append(3) #add 3 to last in list
a.insert(1,5) #insert 5 at index 1
print(a)

#extend list
b = ['a','b','c','d']
a.extend(b) #extend list a with list b
print(a)

#remove list items
a.remove(1) #removes the item 1
print(a)
a.pop(0) #removes the index 0
print(a)
b.clear #clear the list
print(b)

# or
del a[0]
print(a)
del b #delete whole list

# loop
for x in a:
    print(x)

for i in range(len(a)):
    print(a[i])

# list comprehension . copy the list to another list

newlist = []
for x in a:
    newlist.append(x)
print(newlist)


