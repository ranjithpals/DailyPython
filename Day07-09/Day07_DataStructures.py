# List
numlist = [1, 2, 3, 4, 5]

# Reverse a list
numlist.reverse()

# LIST OBJECT METHOD does not RETURN A VALUE
# IT CHANGES THE LIST OBJECT ITSELF, cos LISTS ARE MUTABLE
# The SAME LIST OBJECT is Modified and a NEW OBJECT IS NOT CREATED.
print(numlist)

# ANOTHER WAY TO REVERSE
# Here the list object is subject to a Slicing Operation and this returns
# A NEW LIST OBJECT
rev = numlist[::-1]

print(rev)

# ANOTHER METHOD TO REVERSE IS SORT
# print(type(rev))

rev.sort()
print(rev)

# CONVERT A STRING TO A LIST
mystr = 'Srinika'
l = list(mystr)
print(l)

# REMOVE THE NTH ITEM OF A LIST, if NO INTEGER provided then removes last item
# LIST OBJECT METHOD CHANGES THE LIST OBJECT AND RETURNS THE REMOVED VALUE
m = l.pop(1)
print(l, m)


# INSERT ITEM TO A LIST AT NTH POSITION
l.insert(1, 'r')

print(l)

# DELETE AN ITEM
del l[0]
print(l)

l.insert(0, 'P')
print(l)

l.append('G')
print(l)

# TUPLE
t = (1, 2, 3, 4, 5)
print(t)

# TUPLE IS IMMUTABLE, IT (TUPLE OBJECT ONCE CREATED) CANNNOT BE CHANGED
# ONLY A NEW TUPLE OBJECT CAN BE CREATED
t.append(5)

# Produces an Error