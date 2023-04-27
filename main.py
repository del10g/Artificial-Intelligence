with open("a_list.txt", "r") as file:
    numbers = file.readlines()
    print(set(list(numbers)))
    