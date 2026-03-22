student = {
    "name": "Tanvi",
    "age": 19,
    "branch": "CSE"
}

print("Student dictionary:", student)
print("Name:", student["name"])

student["age"] = 20
print("Updated dictionary:", student)

student.pop("branch")
print("After removing element:", student)

extra_info = {"college": "MIT ADT"}
student.update(extra_info)

print("Merged dictionary:", student)
