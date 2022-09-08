# write a python program to know if a given number is zero, positive or negative.

def nature_of_num(num):
    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positve")
    elif num == 0:
        print("Zero")
    else:
        print(num)

num = 10
nature_of_num(num)