from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

choice = input()

if choice == "c_to_f":
    c = float(input())
    print(celsius_to_fahrenheit.convert(c))

elif choice == "f_to_c":
    f = float(input())
    print(fahrenheit_to_celsius.convert(f))

elif choice == "c_to_k":
    c = float(input())
    print(celsius_to_kelvin.convert(c))

else:
    print("Invalid choice")
