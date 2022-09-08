# Write a program to display group of messages when the conditon is true.

def greet(time):
    if time < 12.00 and time >= 4.00:
        print("Good Morning.")
    elif time >= 12.00 and time <= 18.00:
        print("Good Afternoon.")
    elif time > 18.00 and time < 20.00:
        print("Good Evening.")
    else:
        print("Good Night.")

greet(23.00)