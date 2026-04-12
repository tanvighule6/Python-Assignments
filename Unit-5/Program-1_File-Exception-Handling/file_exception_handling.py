filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied. Cannot read the file.")

except Exception as e:
    print("Some other error occurred:", e)
