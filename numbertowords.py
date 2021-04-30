import math


def number_to_words(number):
    dict = {0: "Zero", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    words = ""


    while number > 0:
        last_digit = number % 10


        number = math.floor(number/10)


        words = dict[last_digit] + words 

    return words




number = [874, 543]
a = []

for i in range(len(number)):
    words = number_to_words(number[i])
    a.append(words)

print(a)
str = ','
print(str.join(a))
