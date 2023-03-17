{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "abda7c7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 17 list comprehensiion problems in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bc7533a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d21d416e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example for loop solution to add 1 to each number in the list\n",
    "numbers_plus_one = []\n",
    "for number in numbers:\n",
    "    numbers_plus_one.append(number + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "83864cec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 18, 20, 24, 257, -7, -3, -1, 6, -8]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers_plus_one"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ec5dc14d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 18, 20, 24, 257, -7, -3, -1, 6, -8]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Example of using a list comprehension to create a list of the \n",
    "# numbers plus one.\n",
    "numbers_plus_one = [number + 1 for number in numbers]\n",
    "numbers_plus_one"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a554b576",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Example code that creates a list of all of the list of strings \n",
    "# in fruits and uppercases every string\n",
    "output = []\n",
    "for fruit in fruits:\n",
    "    output.append(fruit.upper())\n",
    "output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "56795f9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1 - rewrite the above example code using list \n",
    "# comprehension syntax. Make a variable named uppercased_fruits \n",
    "# to hold the output of the list comprehension. Output should be \n",
    "# ['MANGO', 'KIWI', etc...]\n",
    "output2 = [fruit.upper() for fruit in fruits]\n",
    "output2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fa45ccb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Mango'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - create a variable named capitalized_fruits and \n",
    "# use list comprehension syntax to produce output like \n",
    "# ['Mango', 'Kiwi', 'Strawberry', etc...]\n",
    "fruits[0][0].upper() + fruits[0][1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "14292350",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin orange']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "capitalized_fruits = [fruit[0].upper() + fruit[1:] for fruit in fruits]\n",
    "capitalized_fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f1139e8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['guava', 'pineapple', 'mandarin orange']"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - Use a list comprehension to make a variable named \n",
    "# fruits_with_more_than_two_vowels. Hint: You'll need a way to \n",
    "# check if something is a vowel.\n",
    "\n",
    "# num_vowels counts the number of vowels (aeiou) in the passed word\n",
    "# and returns the count. if word is not a string, returns 0\n",
    "def num_vowels(word):\n",
    "    if type(word) != str: return 0\n",
    "    word = word.lower()\n",
    "    count = 0\n",
    "    for c in word:\n",
    "        if c in 'aeiou':\n",
    "            count += 1\n",
    "    return count\n",
    "fruits_with_more_than_two_vowels = [fruit for fruit in fruits if num_vowels(fruit) > 2]\n",
    "fruits_with_more_than_two_vowels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ae133b71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num_vowels(7.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6411de7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
