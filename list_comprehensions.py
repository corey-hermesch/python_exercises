#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[2]:


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)


# In[4]:


# Example of using a list comprehension to create a list of the numbers
# plus one.
numbers_plus_one = [number + 1 for number in numbers]


# In[5]:


# Example code that creates a list of all of the list of strings in 
# fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    


# In[8]:


# Exercise 1 - rewrite the above example code using list comprehension 
# syntax. Make a variable named uppercased_fruits to hold the output 
# of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
output = []
output = [fruit.upper() for fruit in fruits]
output


# In[9]:


# Exercise 2 - create a variable named capitalized_fruits and use list 
# comprehension syntax to produce output like ['Mango', 'Kiwi', 
# 'Strawberry', etc...]
capitalized_fruits = [fruit[0].upper() + fruit[1:] for fruit in fruits]
capitalized_fruits


# In[18]:


# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check 
# if something is a vowel.
def num_vowels(word):
    count_vowels = 0
    for c in word.lower():
        if c in 'aeiou':
            count_vowels += 1
    return count_vowels

fruits_with_more_than_two_vowels = []
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (
                                    num_vowels(fruit) >= 2)]
fruits_with_more_than_two_vowels


# In[20]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if (
                                    num_vowels(fruit) == 2)]
fruits_with_only_two_vowels


# In[21]:


# Exercise 5 - make a list that contains each fruit with more than 5 
# characters
fruits_with_more_than_5_chars = [fruit for fruit in fruits if (
                                 len(fruit) > 5)]
fruits_with_more_than_5_chars


# In[22]:


# Exercise 6 - make a list that contains each fruit with exactly 5
# characters
fruits_with_more_5_chars = [fruit for fruit in fruits if (
                                 len(fruit) == 5)]
fruits_with_more_5_chars


# In[23]:


# Exercise 7 - Make a list that contains fruits that have less than 5 
# characters
fruits_with_less_than_5_chars = [fruit for fruit in fruits if (
                                 len(fruit) < 5)]
fruits_with_less_than_5_chars


# In[24]:


# Exercise 8 - Make a list containing the number of characters in each 
# fruit. Output would be [5, 4, 10, etc... ]
fruit_char_length_list = [len(fruit) for fruit in fruits]
fruit_char_length_list


# In[25]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains
# a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
fruits_with_letter_a


# In[36]:


# Exercise 10 - Make a variable named even_numbers that holds only the 
# even numbers 
even_numbers = [x for x in numbers if x % 2 == 0]
even_numbers


# In[37]:


# Exercise 11 - Make a variable named odd_numbers that holds only the 
# odd numbers
odd_numbers = [x for x in numbers if x % 2 == 1]
odd_numbers


# In[38]:


# Exercise 12 - Make a variable named positive_numbers that holds only 
# the positive numbers
pos_numbers = [x for x in numbers if x > 0]
pos_numbers


# In[40]:


# Exercise 13 - Make a variable named negative_numbers that holds only 
# the negative numbers
negative_numbers = [x for x in numbers if x < 0]
negative_numbers


# In[41]:


# Exercise 14 - use a list comprehension w/ a conditional in order to 
# produce a list of numbers with 2 or more numerals
test_list = [1, -1, 0, 25, 100, -42, 16]
two_plus_nums = [x for x in numbers if (
                 len(str(x).strip('-')) >= 2)]
two_plus_nums


# In[42]:


# Exercise 15 - Make a variable named numbers_squared that contains 
# the numbers list with each element squared. 
# Output is [4, 9, 16, etc...]
numbers_squared = [x ** 2 for x in numbers]
numbers_squared


# In[43]:


# Exercise 16 - Make a variable named odd_negative_numbers that 
# contains only the numbers that are both odd and negative.
odd_negative_numbers = [x for x in numbers if (x < 0) and (x % 2 == 1)]
odd_negative_numbers


# In[44]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a 
# list containing each number plus five. 
numbers_plus_5 = [x + 5 for x in numbers]
numbers_plus_5


# In[63]:


# BONUS Make a variable named "primes" that is a list containing the 
# prime numbers in the numbers list. *Hint* you may want to make or 
# find a helper function that determines if a given number is prime 
# or not.

# is_prime will take a positive integer and return True if it is prime
# and false if it is not prime
# A google search helped me optimize this function. 
# BL, we only have to check for no remainder up to the square root of y
def is_prime(y):
    if y <= 1: 
        return False
    for i in range(2,int(y ** .5 + 1)):
        if y % i == 0:
            return False
    return True

primes = [x for x in numbers if is_prime(x)]
primes


# In[64]:


numbers


# In[ ]:




