#filter()
#filter () selects elements from an iterable that satisfy a given condition

nums = [35,65,95,80]
evens = filter(lambda x: x > 40, nums)
even1=list(evens)
print("evens:", even1)