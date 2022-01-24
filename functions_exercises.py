
#1
from statistics import _NumberT


def is_two (x):
    if x in [2, '2']:
        return True
    else:
        return False

 # Test
 is_two(2)

#2
def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']:
        return result
    else:
        return False

 # Test
 is_vowel(a)

#3
def is_consonant (letter):
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        return False
    else:
        return True

 # Test
 is_consonant(a)

 #4
def first_letter(word):
    if is_consonant(word[0]) == str:
         return capitalize(word)
    else:
        return word



#5
def calculate_tip(bill_amount, tip_percent):
    if type(bill_amount) != float:
        return False
    if tip_percent < 0 or tip_percent >1:
        return 'must be between 0 and 1'
    return tip_percent * bill_amount
# Test
calculate_tip(84, .2)

#6
def apply_discount(original_price, discount_percent):
    discounted_price = original_price * discount_percent
    return discounted_price

# Test
apply_discount (105, .1)

#7
def handle_commas(number_string):
    if type(somestring):
        return 'input must be a string'
    somestring = somestring.replace(',', '') 
    if somestring.isdigit():   
        return float(somestring)
    else:
        return 'Input must be a string that is a number'

handle_commas(1,234,567,890)


# Test - Won't work?!!! **********
handle_commas(1,234,456,678,890)

#8
def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    if 80<= grade <= 89:
        return 'B'
    if 70 <= grade <= 79:
        return 'C'
    if 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

get_letter_grade(87)

#9
def remove_vowels (word):
    if typr(word) != str:
        return False
    output = ''
    for letter in word:
        if is_consonant(letter):
            output += letter

remove_vowels("banana")

#10
def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output

normalize_name("First Name")

#11
somenums = [1, 2, 3, 4, 5]

for i, num in enumerate(somenums):
    print('index: ', i)
    print(num)

def cumulative_sum (somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
