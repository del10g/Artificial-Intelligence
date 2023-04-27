import random

class Agorithm:
    def __init__(self):
        print("Satrt Running a text algorithm")
        self.len_of_list = input("Enter the length of the list: ")
        self.high = int(input("Enter the high number: "))
        self.a_list = list()
        for i in range(int(self.len_of_list)):
            self.a_list.append(random.randint(1, self.high))

    def bubble_sort(self):
        for i in range(len(self.a_list) - 1):
            for j in range(len(self.a_list) - 1 - i):
                if self.a_list[j] > self.a_list[j + 1]:
                    self.a_list[j], self.a_list[j + 1] = self.a_list[j + 1], self.a_list[j] 
        print(self.a_list)
    def insertion_sort(self):
        for i in range(1, len(self.a_list)):
            key = self.a_list[i]
            j = i - 1
            while j >= 0 and self.a_list[j] > key:
                self.a_list[j + 1] = self.a_list[j]
                j -= 1
            self.a_list[j + 1] = key
        print(self.a_list)

al = Agorithm()
# al.bubble_sort()
al.insertion_sort()
with open("a_list.txt", "w") as f:
    f.write(str(al.a_list))