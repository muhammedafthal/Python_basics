
# This would become error. Because we're just trying to change its letter from the value.
# So, the string is Immutable.
"""
name1 = "Muhammed Afthal K"
name1[4] = "L"
print(name1)
"""
# This would become work. Because its value just changed.
name2 = "Muhammed Aslam K A"
name2 = "Muhammed Bilal K A"
print(name2)

# This is not an error. Because the index value were just changed that's it.
# So, the array is Mutable.
list = ["Crossroads", "SPF", "Python"]
list[1] = "Brototype"
print(list)
print(list[-1])
print(list[-2:])
print(list[0:])

# Just inserting some values into the list array.
list = list + ["Muhammed Afthal K", 10]
print(list)

# For place the value at the end of the array.
list.append("C++")
print(list)

list.append(input("Enter a value"))
print(list)