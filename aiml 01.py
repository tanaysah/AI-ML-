#write a function that accepts a number from user and prints whether the number is odd even.


def check_odd_even():
    n = int(input("Enter niumber: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_odd_even()
