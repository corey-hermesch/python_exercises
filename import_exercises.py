#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1a. import the function_exercises module
import function_exercises as fe


# In[2]:


# 1a. call is_vowel using the . syntax
fe.is_vowel('a')


# In[3]:


# 1b. use from to import calculate_tip function
from function_exercises import calculate_tip


# In[4]:


# 1b. call calc_tip
calculate_tip(.2, 100)


# In[5]:


# 1c. use from to import get_letter_grade and give it an alias
from function_exercises import get_letter_grade as get_lg


# In[6]:


# 1c. test get_lg
get_lg(99)


# In[7]:


#2. use itertools module
import itertools as iter


# In[16]:


#2.  Use the itertools modue from the python standard library. 
#2a. How many different ways can you combine a single letter from "abc"
#    with either 1, 2, or 3

# To just get the number of combinations multiply the number
# of choices of 1 letter from 'abc' * the number of choices from '123'

# obtain lists of possible 1-character permuations (in this case 
# combinations would also have worked since it is 1 character)
x1 = list(iter.permutations('abc', 1))
x2 = list(iter.permutations('123', 1))

# multiply the length of x1 * the length of x2
numb_combos = len(x1) * len(x2)
print("There are", numb_combos, "ways to combine 'abc' with either a 1, 2, or 3")


# In[117]:


#2a. continued. In order to get a list with all the unique combinations 
# that start with a single letter from "abc" and combine with a 1, 2 or 3
# we have to do some other work:

# put a list of the 2-character permutations of 'abc123' in x3
x3 = list(iter.permutations('abc123', 2))

# x3 is now a list of tuples like [('a', 'b'), ac, a1, ...]
# We are only interested in the combinations that start with a letter and 
# end with a number. So make a list of those strings
combo_list = [t[0]+t[1] for t in x3 if t[0].isalpha() and t[1].isdigit()]

# print the list for good measure and the length of the list which is the
# answer we were looking for
print(combo_list)
print("There are", len(combo_list), "ways to combine 'abc' with either a 1, 2, or 3")


# In[28]:


# 2b. How many different combinations are there of 2 letters from abcd?

# use itertools.combinations function to create a list of combinations
combo_list2 = list(iter.combinations('abcd', 2))
# print the list for good measure and the length of the list which is our answer
combo_list2
print("There are", len(combo_list2), "2-character combinations of 'abcd'.")


# In[29]:


# 2c. How many different permutations are there of 2 letters from "abcd"?

# same logic as 2b
combo_list3 = list(iter.permutations('abcd', 2))
print("There are", len(combo_list3), "2-character permutations of 'abcd'.")
combo_list3


# In[30]:


#3 Save a file called profiles.json. import json and use the provided
# code to load/open the text from profiles.json
import json
# bring in a list of dictionaries into profiles
profiles = json.load(open('profiles.json'))


# In[37]:


# just a quick look at the names before we start on the questions
for profile in profiles:
    print(profile['name'])


# In[39]:


#3a: What is the total number of users?
print("There are", len(profiles), "users.")


# In[43]:


#3b. What is the number of active users?

# review what the keys are
profiles[0].keys()
# isActive is the key I need; confirm it is a boolean
type(profiles[0]['isActive'])
# initialize a count variable
count_active = 0
# use a for loop to count the number of times isActive is True
for profile in profiles:
    if profile['isActive']:
        count_active += 1
print("There are", count_active, "active users.")


# In[44]:


#3c. What is the total number of inactive users?

# same logic as 3b
# initialize a count variable
count_inactive = 0
# use a for loop to count the number of times isActive is False
for profile in profiles:
    if not profile['isActive']:
        count_inactive += 1
print("There are", count_inactive, "inactive users.")


# In[53]:


#3d What is the grand total of balances for all users

# review what the keys are
profiles[0].keys()
# balance is the key I need; confirm it is a float
profiles[0]['balance']
# it is a string <sigh>

# define function to change string money to float
def moneystr_to_dec(m_str):
    m_var = ''
    for c in m_str:
        if c.isdigit() or c == '.':
            m_var += c
    return float(m_var)

# test function
moneystr_to_dec('$2,097.02')


# In[119]:


#3d continued. What is the grand total of balances for all users

# define a function to return the grand total
# sum_balance takes in a list of dictionaries such that each 
# each dictionary in the list has a 'balance' key with a 
# string representing the balance (example '$2,079.22')
def sum_balances(profiles):
    # initialize a summing variable
    total_balance = 0.0
    # for each profile's balance, change it to a float and add it to total
    for profile in profiles:
        total_balance += moneystr_to_dec(profile['balance'])
    return total_balance

# I want to use fstring, so I put the sum in a variable grand_total
grand_total = sum_balances(profiles)
# print the answer
print(f"The grand total of balances is ${grand_total}.")


# In[120]:


#3e What is the average balance per user
# use sum_balances function and divide by len of profiles
avg_balance = round(sum_balances(profiles) / len(profiles), 2)
print(f"The average balance of all users is ${avg_balance}.")


# In[66]:


#3f Who is the user with the lowest balance?

min_balance = moneystr_to_dec(profiles[0]['balance'])
min_b_user = profiles[0]['name']
for profile in profiles:
    n = moneystr_to_dec(profile['balance'])
    if n < min_balance:
        min_balance = n
        min_b_user = profile['name']

print (f"The minimum balance of all users is {min_b_user} with ${min_balance}")


# In[67]:


#3f Who is the user with the max balance?

max_balance = moneystr_to_dec(profiles[0]['balance'])
max_b_user = profiles[0]['name']
for profile in profiles:
    n = moneystr_to_dec(profile['balance'])
    if n > max_balance:
        max_balance = n
        max_b_user = profile['name']

print (f"The maximum balance of all users is {max_b_user} with ${max_balance}")


# In[93]:


#3g What is the most common favorite fruit
# looks like pandas dataframe.mode will be useful, but I'll wait

# define a function to return a list of fruits
def make_fruit_list(profiles):
    fruit_list = []
    for profile in profiles:
        fruit_list.append(profile['favoriteFruit'])
    return fruit_list

# define a function to return a list of lists of strings (fruits) and their count.
# input is a list of strings. output list will look like this:
# [['strawberry', 6], ['banana', 5], ...]

def count_fruits(fruit_list):
    # sort the list to group unique fruits together
    fruit_list.sort()
    # use a while loop to make a list of lists with form [['fruit_name', fruit_count], [], ...]
    # first initialize 3 things: the final product fruit_count_list, an index variable
    # and a count variable.  i_index counts through the sorted fruit_list.
    # j_count will count the number of times a unique fruit is in fruit_list
    fruit_count_list = []
    i_index = 1
    j_count = 1
    # while i_index is less than the length of the fruit_list, keep going
    while i_index < len(fruit_list):
        # if the current i_index item is the same as the previous one add one to j_count
        if fruit_list[i_index] == fruit_list[i_index - 1]:
            j_count += 1
        # if we find a new fruit, then I want to append the old fruit + the j_count to 
        # my output list and reinitialize my j_count
        else:
            fruit_count_list.append([fruit_list[i_index -1], j_count])
            j_count = 1
        # increment our looping variable to keep going through the list
        i_index += 1    
    # the last iteration of the while loop will not hit the else statement, so
    # I append the last fruit and j_count outside the loop
    fruit_count_list.append([fruit_list[i_index -1], j_count])
    return fruit_count_list


# In[121]:


#3g continued. What is the most common favorite fruit

# my solution is to make a list of lists; the inner lists will be
# a unique fruit_name and a count of the number of times
# that fruit_name appears. Then I will iterate over the outer list
# to take the max of those counts and the associated fruit

# make a list of all the favorite fruits of users
fruit_list = make_fruit_list(profiles)

# make a list of lists of [unique_fruit, count]
fruit_count_list = count_fruits(fruit_list)

# now we are ready to iterate over our new list and find the fruit that 
# is the most common
# initialize max_fruit which will be the name of the fruit, i.e. a string
# to be the first fruit in the list of lists
max_fruit = fruit_count_list[0][0]
# initialize max_fruit_count to be the first count in the list of lists
max_fruit_count = fruit_count_list[0][1]
# go through the fruit_count_list
for fruit_ls in fruit_count_list:
    # if the count of the next fruit is greater than our current max, update
    # our variables with the new max_fruit_count and new max_fruit name
    if fruit_ls[1] > max_fruit_count:
        max_fruit_count = fruit_ls[1]
        max_fruit = fruit_ls[0]

# finally print the answer
print(f"The most common favorite fruit is {max_fruit} with {max_fruit_count} occurrences.")


# In[95]:


#3f What is the least common favorite fruit?

# make a list of all the favorite fruits of users
fruit_list = make_fruit_list(profiles)

# make a list of lists of [unique_fruit, count]
fruit_count_list = count_fruits(fruit_list)

# now we are ready to iterate over our new list and find the fruit that 
# is the least common. # use same logic as 3e
min_fruit = fruit_count_list[0][0]
min_fruit_count = fruit_count_list[0][1]
for fruit_ls in fruit_count_list:
    if fruit_ls[1] < min_fruit_count:
        min_fruit_count = fruit_ls[1]
        min_fruit = fruit_ls[0]

# finally print the answer
print(f"The least common favorite fruit is {min_fruit} with {min_fruit_count} occurrences.")


# In[112]:


#3g What is the total number of unread messages for all users

# the number of unread messages is contained in the 'greeting' value
# each greeting is standardized with a greeting followed by the text
# "You have (x or xx or xxx or ...) unread messages"
# so we need to look at each greeting, parse it to get that number
# in a string format, make it an int, and sum the int values

# define a function to return the integer value for the number
# of unread messages from a greeting string of the format:
# "Hello, first_name last_name! You have xxx unread messages"
def get_message_int(greeting_string):
    # getting the last 28 characters in the string
    # this will work unless there is an obscenely large number of 
    # unread messages or if the greeting_string is not in the
    # standard format described above
    greeting_string = greeting_string[-28:]
    # initialize the variable str_digit
    str_digit = ''
    # go through greeting_string and collect the digits
    for c in greeting_string:
        if c.isdigit():
            str_digit += c
    # finally return an integer of our collected digits
    return int(str_digit)
    


# In[116]:


#3g continued. What is the total number of unread messages for all users

# initialize our count variable to 0
message_count = 0
# iterate for each dictionary (profile) in the list of dictionaries (profiles)
for profile in profiles:
    # add in the integer value of unread messages from the greeting string
    message_count += get_message_int(profile['greeting'])

# print the answer
print(f"The total number of unread messages for all users is {message_count}")


# In[63]:


# review what the keys are
profiles[0].keys()

