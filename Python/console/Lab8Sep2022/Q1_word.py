# Write a program in python to express a digit in a word.

def digit_to_word(num):
    num_to_word = {
        "1" : "One",
        "2" : "Two",
        "3" : "Three",
        "4" : "Four",
        "5" : "Five",
        "6" : "Six",
        "7" : "Seven",
        "8" : "Eight",
        "9" : "Nine",
        "0" : "Zero"
    }

    final_words = ""
    for digit in num:
        final_words += num_to_word[digit] + " "
    print(final_words)
    
num = input("Enter your numbers ")

digit_to_word(num)