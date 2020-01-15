"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
fourSlice = slice(1,2)
aSlice = a[fourSlice]
for item in aSlice:
    print(int(item))

# Output the second-to-last element: 9
nineSlice = slice(4, 5)
sliceTheNine = a[nineSlice]
for item in sliceTheNine:
    print(int(item))

# Output the last three elements in the array: [7, 9, 6]
lastThreeSlice = slice(3, None)
print(a[lastThreeSlice])

# Output the two middle elements in the array: [1, 7]
middleSlice = slice(2,4)
print(a[middleSlice])

# Output every element except the first one: [4, 1, 7, 9, 6]
exceptTheFirst = slice(1, None)
print(a[exceptTheFirst])

# Output every element except the last one: [2, 4, 1, 7, 9]
exceptTheLast = slice(0,5)
print(a[exceptTheLast])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
worldSlice = slice(7, 12)
sliceTheWorld = s[worldSlice]
stringifyWorld =  (F"{sliceTheWorld}")
print(stringifyWorld)