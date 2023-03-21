#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Prompt the user for a day of the week, print out whether the day 
# is Monday or not

response = input("What day of the week is it?  ")
if response.lower() == 'monday': 
    print("It is Monday.")
else: 
    print("It is not Monday!")


# In[1]:


# Prompt the user for a day of the week, print out whether the day is 
# a weekday or a weekend
new_response = input("What day of the week is it?  ")
if (new_response.lower() == "saturday"
    or new_response.lower() == "sunday"):
    print("It's the weekend!")
else: 
    print("It is a weekday.")
        


# In[15]:




# Calculate a weekly paycheck, accounting for overtime pay. 
# Create variables and make up values for:

#     The number of hours worked in one week
#     The hourly rate

# For calculating pay:

#     For working 40 hours or less, each hour is paid at the 
#     hourly rate

#     For working more than 40 hours

#         the first 40 hours are paid at the hourly rate

#         each hour after 40 is paid at time and a half 
#         (hourly rate * 1.5)

hours_worked = 39
hour_rate = 10
if hours_worked <= 40:
    weekly_paycheck = hours_worked * hour_rate
else:
    weekly_paycheck = 40 * hour_rate + (hours_worked - 40) * hour_rate * 1.5
weekly_paycheck    


# In[16]:


# create a while loop that runs so long as i < = 15; 
# start i at 5, print it and increment i by 1 each time
i = 5
while i <= 15:
    print(i)
    i += 1


# In[19]:


# create a while loop that counts by 2 starting with 0, end at 100
i = 0
while i <= 100:
    print(i)
    i += 2


# In[9]:


# create a while loop that prints a number (starting at 2),
# then squares the number. It continues while the number is < 1000000
i_square = 2
while i_square < 1_000_000:
    print(i_square)
    i_square **= 2   # short hand for i_square = i_square ** 2


# In[25]:


# create a while loop that prints a number and decrements by 5 until
# the number is < 5; start at 100
i = 100
while not(i<5):
    print(i)
    i -= 5


# In[24]:


# create a for loop that asks a user for a number then creates a 
# multiplication table for that number from 1 to 10

response = int(input("Please enter a number between 1 and 10: "))
for i in range(1,11):
    print(response, " x ", i, " = ", response * i)
    # print()
    # print(f'{i} x ', response, f' = {i*int(response)}')
        


# In[26]:


# create a for loop that uses print to create 1 22 333 ... to 9
for i in range(1,10):
    print_str = ""
    for j in range (1,i+1):
        print_str = print_str + (str(i))
    print(print_str)

    # could have used: print(str(i)*i)
        


# In[30]:


# write a program that prompts the user for a positive integer
# then print out the integers from the entered value down to 1
# decrementing by 1
# use break
response = int(input("Please enter a positive integer: "))
if response > 0:
    while True:
        print(response)
        response -= 1
        if response < 1:
            break
else:
    print("Invalid input")
    


# In[31]:


# write a program that prompts the user for a positive integer
# then print out the integers from 0 to that integer counting by 1
# use break

x = int(input("Please enter a positive integer: "))
i = 0
while True:
    print(i)
    i += 1
    if i > x: break


# In[4]:


# prompt user for an odd number between 1 and 50
# use a loop and a break statement to continue prompting the user
# if they enter an invalid input (hint: isdigit)
# use a loop and a continue statement to print all odd numbers 
# between 1 and 50, skipping the number the user entered

# we are using a break statement to stop the while loop
# so, it will run indefinitely unless we meet the break conditions
while True:
    # ask for user input
    user_input = input("Please enter an odd integer between 1 and 50: ")

    # isdigit() returns true for positive integers
    if user_input.isdigit():
        n = int(user_input)

        # test if n is within range and odd
        if (n <= 0) or (n >= 50) or (n % 2 != 1): 
            print("Invalid input (not odd or not in range 1-50)")
        else: 
            break

    # if isdigit() returned false, give the user feedback
    else:
        print("Invalid Input (not a positive integer)")

i = 1
while i < 50:
    if i == n:
        print("Yikes! Skipping number:", n)
    else:
        print(i)
    i += 2
        


# In[1]:


# FizzBuzz test
for i in range(1,101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
            continue
        else: 
            print("Fizz")
            continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)
    
    


# In[22]:


# 4. Display a table of powers (x ** 0, x ** 2, x ** 3); assume valid input

while True:
    user_input = int(input("What number would you like to go up to? "))
    print("Here is your table!")
    print()
    print("number | squared | cubed")
    print("------ | ------- | -----")
    for i in range(1,user_input+1):
        print('{:<6d}'.format(i), 
              "|", '{:<7d}'.format(i ** 2), 
              "|", '{:<5}'.format(i ** 3)
             )
    is_continue = input("Would you like to continue? (Y/N) ")
    if is_continue.lower() != 'y':
        break


# In[28]:


# ask for input (0-100) and display appropriate letter grade
# associated with input. assume valid integer inputs
while True: 
    user_input = int(input("Please enter the student's numerical grade (0-100): "))
    while True:
        if user_input <= 59: 
            print('F')
            break
        if user_input <= 61: 
            print('D-')
            break
        if user_input <= 64: 
            print('D')
            break
        if user_input <= 66: 
            print('D+')
            break
        if user_input <= 68: 
            print('C-')
            break
        if user_input <= 77: 
            print('C')
            break
        if user_input <= 79: 
            print('C+')
            break
        if user_input <= 81: 
            print('B-')
            break
        if user_input <= 85: 
            print('B')
            break
        if user_input <= 87: 
            print('B+')
            break
        if user_input <= 89: 
            print('A-')
            break
        if user_input <= 98: 
            print('A')
            break
        if user_input <= 100: 
            print('A+')
            break
        break
    is_continue = (input("Continue? (Y/N)"))
    if is_continue.lower() != 'y':
        break


# In[3]:


# create a list of dictionaries
# each dictionary represents a book
# each dictionary will have keys: title, author, genre
# loop through the list and print out info about each book
d1 = {'title': "Lillith's Brood",
      'author': "Octavia Butler",
      'genre': "Science Fiction"}
d2 = {'title': "Glucose Revolution",
      'author': "Jessica Inchauspe",
      'genre': "Self Help"}
d3 = {'title': "Dare to Lead",
      'author': "Brene Brown",
      'genre': "Leadership"}
d4 = {'title': "Devolution: A Firsthand Account of the Ranier Sasquatch Massacre",
      'author': "Max Brooks",
      'genre': "Fiction"}
d5 = {'title': "The Ploughmen",
      'author': "Kim Zupan",
      'genre': "Fiction"}

ls = [d1, d2, d3, d4, d5]

for book in ls:
    print("Title:  ", book['title'])
    print("Author: ", book['author'])
    print("Genre:  ", book['genre'])
    print()
    
while True:
    user_input = input("Enter a genre: ")
    for book in ls:
        if book['genre'] == user_input:
            print()
            print("Title:  ", book['title'])
            print("Author: ", book['author'])
            print("Genre:  ", book['genre'])
    print()        
    is_continue = input("Continue? Y/N ")
    print()
    if is_continue.lower() != 'y':
        break


# In[6]:


print(f"{ls[0]['title']} is a book title.")


# In[18]:


new_list = [x for x in range(1,10,2)]
new_list


# In[33]:


f'Skip this number: {7}'


# In[ ]:




