#filter()
#filter () selects elements from an iterable that satisfy a given condition

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, nums)
even1=list(evens)
print("evens:", even1)