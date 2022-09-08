# write a python program to test  whether a given number is even or odd

def even_or_odd(num):
    if((num ^ 1) == num + 1):
        print(True)
    else:
        print(False)

num = 43
even_or_odd(num)