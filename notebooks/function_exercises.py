#1. define a function is_two, input a string or number; 
# return True if it is '2', 2, 2.0
def is_two(a):
    # if the input is a string return false if it's not a number
    if type(a) == str:
        if not a.isdigit():
            return False 
    # at this point, we know we have a number or a string that's a number
    # so test the equality of the float version to 2.0 and return
    # that T/F value
    return float(a) == 2.0

print(is_two(2))
print(is_two(0))
print(is_two(-1))
print(is_two(2.5))
print(is_two(2.0))
print(is_two('2'))
print(is_two('2.0'))
print(is_two('coffee'))

#1 with lambda function without taking the float case into account
is_two = lambda a: int(a) == 2

print(is_two(2))
print(is_two(0))
print(is_two(-1))

#2. define function is_vowel, assume letter input
# returns true if the letter input is a vowel (aeiou, not y)
def is_vowel(a):
    return a.lower() in "aeiou"

# testing function 
print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('x'))

#3 define is_consonant, use is_vowel, assume letter input
# returns true if the letter input is a consonant
def is_consonant(a):
    return not is_vowel(a)

# testing function
print(is_consonant('a'))
print(is_consonant('b'))

#4 define function to capitalize first letter of a word if the letter is a consonant
# assumes string input
def cap_first_consonant(word):
    # uses is_consonant function to test if first letter of word is a consonant
    if is_consonant(word[0]):
        # if true, return the word with the first letter capitalized via title method
        return word.title()
    else:
        # if false, just return the word back
        return word

# testing function
print(cap_first_consonant("hello"))
print(cap_first_consonant("ello"))
print(cap_first_consonant("allo"))

#5 define calculate_tip; inputs are tip percent (decimal) and total bill; return amount to tip
# assumes number inputs and percent should be between 0 and 1 (10% = .1)
def calculate_tip (percent, total):
    return total * percent

# testing function
print (calculate_tip(.2, 100))

#6 define apply_discount; inputs are original price and discount % (decimal);
#  returns price after discount has been applied
#  assumes number inputs, discount should be a decimal between 0 and 1
def apply_discount(price, discount):
    return price - (price * discount)

# testing function
print (apply_discount(100, .2))

#7 define handle_commas; input is string that is a number with commas;
# returns an int with no commas
def handle_commas(num_string):
    return int(num_string.replace(',',''))

# testing function
print(handle_commas('100,101,200'))

#8 define function get_letter_grade; input number (0-100); return letter grade (A-F)
# assumes input is a number between 0 and 100
def get_letter_grade(x):
    if x >= 90: return 'A'
    if x >= 80: return 'B'
    if x >= 70: return 'C'
    if x >= 60: return 'D'
    return 'F'

# testing function
print(get_letter_grade(55))
print(get_letter_grade(67))
print(get_letter_grade(90))

#9 define remove_vowels; input string; return string with all vowels removed
def remove_vowels(word):
    # cons_list is a list of all the characters in
    # the string word that are consonants and not vowels
    # cons_list will be used to iterate over
    cons_list = [c for c in word if is_consonant(c)]
    # initialize new_word
    new_word = ''
    # make a new string out of the cons_list list of consonants
    for c in cons_list:
        new_word += c
    return new_word

# testing functioin
print(remove_vowels('letter'))


#10 def normalize_name; input string, return valid python identifier such that:
# remove leading/trailing whitespace, spaces become underscores, all lowercase
# for example Name becomes name, First Name becomes first_name, % completed becomes completed
def normalize_name(input_name):
    # first, strip() gets rid of leading and trailing whitespace
    input_name = input_name.strip()
    # define a string of all the characters to remove
    chars_to_remove = "!@#$%^&*()+=[]{}|/\,:;.`~"
    # for every character in chars_to_remove, remove it from the input_name
    for c in chars_to_remove:
        input_name = input_name.replace(c, "")
    # additionally, replace all spaces with underscores
    input_name = input_name.replace(' ', '_')
    # lastly, make it lower case and return
    return input_name.lower()

# testing function
test = "   sev%&3@@1 dK())"
print(normalize_name(test))

#11 def cumulative_sum; input list of numbers; return a list of "cumulative sums" such that
# cumulative_sum([1,1,1]) returns [1,2,3]
# cumulative_sum([1,2,3,4]) returns [1,3,6,10]
def cumulative_sum(num_list):
    # initialize a new_list and the cumulative sum
    new_list = []
    cum_sum = 0
    # for each number x in the input list, append x + cum_sum to new_list
    # and update cum_sum
    for x in num_list:
        new_list.append(x + cum_sum)
        cum_sum += x
    return new_list

# testing function
num_list = [1,2,3,4]
test_list = [-4, 0, 4, 100]
print(cumulative_sum(num_list))
print(cumulative_sum(test_list))

# Bonus 1. define function twelveto24; input a string in the format
# 10:45am or 4:30pm (h:mmam or h:mmpm) and return a string in 24-hour
# format. 10:45am becomes 1045, 4:30pm becomes 1630

# def twelveto24(time_str):

#     if time_str[-2] == 'a':
#         time_str = time_str.replace(':', '')
#         time_str = time_str.replace('am', '')
#         time_int = int(time_str) + 1200
#         return str(time_int)
#     elif time_str[-2] == 'p'
#     return
