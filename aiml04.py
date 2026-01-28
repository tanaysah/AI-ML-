#given a list nums = [ 1 , 2 , 3 , 4 ] write a program using map() to add 1 to every element of list and print the new list.


nums = [1, 2, 3, 4]
new_list = list(map(lambda x: x + 1, nums))
print("New list:", new_list)
