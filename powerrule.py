n = ""
a = ""
c = ""

print("Input an expression in the form: nx^a + c")
while True:
    while n != int():
        try:
            n = int(input("n = "))
            print(str(n) + "x^a + c")    
            break
        except ValueError:
            print("Not an integer! Try again.")
            continue
    while a != int():
        try:
            a = int(input("a = "))
            print(str(n) + "x^" + str(a) + " + c")
            break
        except ValueError:
            print("Not an integer! Try again.")
            continue
    while c != int():
        try:
            c = int(input("c = "))
            print(str(n) + "x^" + str(a) + " + " + str(c))
            break
        except ValueError:
            print("Not an integer! Try again.")
            continue
        break
    break

print("Calculating derivative...")

print("The derivative of: " + str(n) + "x^" + str(a) + " + " + str(c) + " is: ")
print(str(n*a) + "x^" + str(a-1))