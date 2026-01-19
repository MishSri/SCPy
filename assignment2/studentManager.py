student={
    "Srijan": 100,
    "Saswat": 99,
    "Bismay": 88
}
option=int(input("""What do you wish to do?
                 1. Add a new student
                 2. Update existing student marks
                 3. Delete a student
                 : """))
match option:
    case 1:
        name=input("Enter student name: ")
        marks=int(input("Enter studen marks: "))
        student.update({name:marks})
    case 2:
        name=input("ENter student name: ")
        marks=int(input("Enter nre marks: "))
        student[name]=marks
    case 3:
        name=input("Enter student name to be deleted: ")
        student.pop(name)
    case _:
        print("Enter a valid option.")

print(f"Dictionary after operation is: \n{student}")