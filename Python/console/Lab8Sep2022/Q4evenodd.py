# write a python program to accept a number from keyboard and test whether it is even or odd.

def even_or_odd(num):
    if((num ^ 1) == num + 1):
        print(True)
    else:
        print(False)

num = int(input("Enter your numbers "))
even_or_odd(num)