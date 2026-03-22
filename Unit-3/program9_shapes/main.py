import shapes

choice = input("Enter shape name: ")

if choice == "circle":
    r = float(input("Enter radius: "))
    print("Area:", shapes.circle(r))

elif choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", shapes.rectangle(l, w))

elif choice == "triangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", shapes.triangle(l, w))

else:
    print("Invalid shape")
