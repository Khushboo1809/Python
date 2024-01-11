a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))
if a > b and a > c:
    print("a is greatest")
else:
    if a < b and b > c:
        print("b is greatest")
    else:
        if c > a and c > b:
            print("c is greatest")
