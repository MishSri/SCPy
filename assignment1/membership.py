text=input("Input a dtring: ")
toFind=input("Input segment to check: ")
if toFind in text:
    print(f"{toFind} is in {text}")
if toFind not in text:
    print(f"{toFind} is in {text}")
## used two separate if conditions instead of if else to show the use of "in" and "not in"
