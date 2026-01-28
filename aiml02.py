#given two number write a lambda function to return A if a>b and B if b>a.

a = int(input("first number: "))
b = int(input("second number: "))

g = lambda a, b: a \
    if a > b \
    else b

print("Greater number is:", g(a, b))



