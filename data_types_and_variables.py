#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 99.9 is a float
type(99.9)


# In[9]:


# "False" is a str
type("False")


# In[10]:


# False is a bool
type(False)


# In[11]:


# '0' is a str
type('0')


# In[12]:


# 0 is an int
type(0)


# In[13]:


# True is a bool
type(True)


# In[14]:


# 'True' is a str
type('True')


# In[15]:


# [{}] is a list
type([{}])


# In[16]:


# {'a': []} is a dict
type({'a': []})


# In[ ]:


# 2. What data type would best represent the following?

#     A term or phrase typed into a search box
#       str
#     Whether or not a user is logged in
#       bool
#     A discount amount to apply to a user's shopping cart
#       float
#     Whether or not a coupon code is valid
#       bool
#     An email address typed into a registration form
#       str
#     The price of a product
#       float
#     The email addresses collected from a registration form
#       list of strings perhaps
#     Information about applicants to Codeup's data science program
#       dict 


# In[17]:


# Error
'1' + 2


# In[61]:


# 2
6 % 4


# In[19]:


# int
type(6 % 4)


# In[20]:


# type
type(type(6 % 4))


# In[21]:


# error
'3 + 4 is ' + 3 + 4


# In[22]:


# False
0 < 0


# In[23]:


# False
'False' == False


# In[24]:


# False
True == 'True'


# In[25]:


# True
5 >= -5


# In[26]:


# True
True or "42"


# In[27]:


# 1
6 % 5


# In[28]:


# False
5 < 4 and 1 == 1


# In[29]:


# False
'codeup' == 'codeup' and 'codeup' == 'Codeup'


# In[30]:


# Error
4 >= 0 and 1 !== '1'


# In[31]:


# True
6 % 3 == 0


# In[32]:


# True
5 % 2 != 0


# In[33]:


# Error
[1] + 2


# In[34]:


# [1, 2]
[1] + [2]


# In[35]:


# [1, 1]
[1] * 2


# In[36]:


# Error
[1] * [2]


# In[37]:


# True
[] + [] == []


# In[38]:


# Error
{} + {}


# In[40]:


# 5. You have rented some movies for your kids:

#     The Little Mermaid for 3 days
#     Brother Bear for 5 days
#     Hercules for 1 day

# If the daily fee to rent a movie is 3 dollars, 
# how much will you have to pay?
3 * 3 + 5 * 3 + 1 * 3  # OR
(3+5+1) * 3


# In[41]:


# 6. Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook.

# They pay you the following hourly rates:

#     Google: 400 dollars
#     Amazon: 380 dollars
#     Facebook: 350 dollars

# This week you worked: 10 hours for Facebook, 6 hours for Google 
# and 4 hours for Amazon.

# How much will you receive in payment for this week? 
g_rate = 400
a_rate = 380
f_rate = 350
6 * g_rate + 4 * a_rate + 10 * f_rate


# In[62]:


# 7. A student can be enrolled to a class only if the class is 
# not full and the class schedule does not conflict with her 
# current schedule.
is_not_full = True
does_not_conflict = True
can_enroll = is_not_full and does_not_conflict
can_enroll


# In[49]:


# 8. A product offer can be applied only if people buys more 
# than 2 items, and the offer has not expired. Premium members 
# do not need to buy a specific amount of products.
is_premium_member = False
items = 3
is_offer_current = False
offer_applied = (is_premium_member or items > 2) and is_offer_current
offer_applied


# # 9. Continue working in the data_types_and_variables.py file. Use the following code to follow the instructions below:
# 
# username = 'codeup'
# password = 'notastrongpassword'
# 
# Create a variable that holds a boolean value for each of the following conditions:
# 
#     The password must be at least 5 characters
#     The username must be no more than 20 characters
#     The password must not be the same as the username
#     Bonus Neither the username or password can start or end with whitespace
# 

# In[50]:


username = 'codeup'
password = 'notastrongpassword'


# In[63]:


pword_more_than_5_chars = len(password) >= 5
pword_more_than_5_chars


# In[53]:


uname_no_more_than_20_chars = len(username) <= 20
uname_no_more_than_20_chars


# In[56]:


not_same = username != password
not_same


# In[58]:


uname_has_leading_trailing_whitespace = username[0] == ' ' or username[-1] == ' '
uname_has_leading_trailing_whitespace


# In[59]:


pword_has_leading_trailing_whitespace = password[0] == ' ' or password[-1] == ' '
pword_has_leading_trailing_whitespace


# In[ ]:




