#1. define a function is_two, input a string or number; 
# return True if it is '2', 2, 2.0
def is_two(a):
    # if a is a float, we need to test if it is 2.0 or 2.1 or 2.x
    if type(a) == float:
        # 2.1 % 2 == .1 and will return False, but 2.0 % 2 == 0 and 
        # will pass thru to the return statement
        if a % 2 != 0: return False
    # return the condition (True or False) that results from int(a) == 2
    return int(a) == 2

print(is_two(2))
print(is_two(0))
print(is_two(-1))
print(is_two(2.5))

#1 with lambda function without taking the float case into account
is_two = lambda a: int(a) == 2

print(is_two(2))
print(is_two(0))
print(is_two(-1))

#2. define function is_vowel, assume letter input
def is_vowel(a):
    return a.lower() in "aeiou"

print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('x'))

#3 define is_consonant, use is_vowel, assume letter input
def is_consonant(a):
    return not is_vowel(a)

print(is_consonant('a'))
print(is_consonant('b'))

#4 define function to capitalize first letter of a word if the letter is a consonant
def cap_first_consonant(word):
    if is_consonant(word[0]):
        return word.title()
    else:
        return word

print(cap_first_consonant("hello"))
print(cap_first_consonant("ello"))
print(cap_first_consonant("allo"))

#5 define calculate_tip; inputs are tip percent (decimal) and total bill; return amount to tip
def calculate_tip (percent, total):
    return total * percent

print (calculate_tip(.2, 100))

#6 define apply_discount; inputs are original price and discount % (decimal);
#  returns price after discount has been applied
def apply_discount(price, discount):
    return price - (price * discount)

print (apply_discount(100, .2))

#7 define handle_commas; input is string that is a number with commas; return number
def handle_commas(num_string):
    return int(num_string.replace(',',''))

print(handle_commas('100,101,200'))

#8 define function get_letter_grade; input number (0-100); return letter grade (A-F)
def get_letter_grade(x):
    if x >= 90: return 'A'
    if x >= 80: return 'B'
    if x >= 70: return 'C'
    if x >= 60: return 'D'
    return 'F'

print(get_letter_grade(55))
print(get_letter_grade(67))
print(get_letter_grade(90))

#9 define remove_vowels; input string; return string with all vowels removed
def remove_vowels(word):
    cons_list = [c for c in word if is_consonant(c)]
    new_word = ''
    for c in cons_list:
        new_word += c
    return new_word

print(remove_vowels('letter'))


#10 def normalize_name; input string, return valid python identifier such that:
# remove leading/trailing whitespace, spaces become underscores, all lowercase
# for example Name becomes name, First Name becomes first_name, % completed becomes completed
def normalize_name(input_name):
    input_name = input_name.strip()
    chars_to_remove = "!@#$%^&*()+=[]{}|/\,:;.`~"
    for c in chars_to_remove:
        input_name = input_name.replace(c, "")
    input_name = input_name.replace(' ', '_')
    return input_name.lower()

test = "   sev%&3@@1 dK())"
print(normalize_name(test))

#11 def cumulative_sum; input list of numbers; return a list of "cumulative sums" such that
# cumulative_sum([1,1,1]) returns [1,2,3]
# cumulative_sum([1,2,3,4]) returns [1,3,6,10]

def cumulative_sum(num_list):
    new_list = []
    cum_sum = 0
    for x in num_list:
        new_list.append(x + cum_sum)
        cum_sum += x
    return new_list

num_list = [1,2,3,4]
test_list = [-4, 0, 4, 100]
print(cumulative_sum(num_list))
print(cumulative_sum(test_list))
