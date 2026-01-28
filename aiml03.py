# map() function - map () applies a function to every element of an iterable

#map (function, iterable)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list (map(lambda x: x ** 2, nums))
print("squares:", squares)
