fruit_dict = {
    "apple": 150,
    "mango": 100,
    "banana": 60
}

fruit = input("enter fruit : ").casefold()
if fruit in fruit_dict:
    print("fruit is present")
else:
    print("fruit is not present")