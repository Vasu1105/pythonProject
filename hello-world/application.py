print('Hello World')
print('run next this')

number = 77

print(number)
weight = 60
first_name = "Vasundhara"
last_name = "jagdale"

name = first_name + " " + last_name
print(name)

sentence = first_name + " " + last_name + " weight " + str(weight) + " kg"

print(sentence)

# for premetive datatypes in python

# String - str class
# Integer - int class
# Boolean - bool class
# Float - float class

data_type1 = type("ABC")
print(data_type1)

data_type2 = type(10)
print(data_type2)

data_type3 = type(10.5)
print(data_type3)

data_type4 = type(True)
print(data_type4)

# operators
# +, -, *, /, % , ()

# Indexing and slicing strings
sentence = "This is the sentence"
print(sentence)

# how to handle special string
sentence = "I'm coming here"
print(sentence)

sentence = "abcdefg"

# a     b   c   d    e   f
# 0     1   2   3    4   5
# -6    -5 -4   -3  -2  -1
#print 'defg'
print(sentence[3:7])
print(sentence[3:])

# with negative index position
print(sentence[-4:])

# Functions to work with String
sentence = "this is the sentence"

# method is invoked in object where as function is not associated with any object for e.g. print() is not associated with function
# upper case
upper_case = sentence.upper()
print(upper_case)

lower_case = upper_case.lower()
print(lower_case)

capitalize = lower_case.capitalize()
print(capitalize)

# isdigit returns boolean
print(capitalize.isdigit())

sentence = "this is 10"
print(sentence.isdigit())
print(sentence.isalnum()) # since it has spaces it will return false

sentence = "thisis10"
print(sentence.isalnum())

sentence = "10"
print(sentence.isdigit())

#startswith
sentence.startswith("10")
#endswith
sentence = "Check ends with with"
print(sentence.endswith("with"))

# You can use startswith in another way also
print(sentence.startswith("ends", 6))

# Formatting strings using format method
sentence = "The sum of 5 + 10 is {0}".format(50)
print(sentence)

sentence = "The sum of {0} + {1} is {2}".format(5,10,15)
print(sentence)

## Strings are immutable (can not be changed)
my_var = "abcdefg"
print(my_var[0])

#my_var[0] = "b" # this will give error because String is immutable

#so you can only reassign the string. So to replace first character in above case how you can do that is
my_var = "b" + my_var[1:]
print(my_var)

## Find remainder of the number
remainder = 15 % 4
print(remainder)

# Assignment 2:
"""
Use of the below format() method is incorrect for what we are trying to do.
We actually have 10 small, 12 large, and 12 medium boxes.
Write code to correct this:
print("We have {2} small boxes, {2} large boxes, {2} medium boxes".format(10,12,12))
"""

print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10,12,12))

# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.
    NOTE: chars variable will contain only 4 characters
    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>
"""

chars = "[[]]"
word = "Cool"

# Expected Result Printed: [[Cool]]

# Your code below:
result = chars[0:2] + word + chars[2:]
print(result)

# another solution
result = chars[:2] + word + chars[2:]
print(result)

# Assignment 4:
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.
    Example:
    ---------------
    word1 = "Vehicle"
    word2 = "Robot"
    result - ehicleRbot
"""

word1 = "Computer"
word2 = "Truck"

# Expected Result Printed: omputerTuck

# Your code below:
print(word1[1:] + word2[0] + word2[2:])

# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.
    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string
    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>
"""

chars = "<<[]]]" # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]


# Your code below:
mid = int((len(chars)/2))
result = chars[:mid] + word + chars[mid:]
print(result)


# Section #2
# Lists in Python
# Collection - Data structure that can contain multiple values

my_list = [1,2,3,4]
print(type(my_list)) # class of this list so this is another advance data type

#pop - pops last item
print(my_list.pop())

my_list = [1,2,3,4]
my_list.pop(0)
print(my_list)

my_list[0] = 3
print(my_list)

# append - append appends  the data at the end of the list but when we call append it does not return anything. It returns None.
# None is another specific type of data type in Python

my_list = [1, 2, 3, 4]
my_list.append("This is to append")

print(my_list)

#sort
my_list = [2,4,5,6,3]
my_list.sort()

print(my_list)

#reverse
my_list.reverse()
print(my_list)

#slicing the list
print(my_list[2:])

#len
print(len(my_list))

#merging list
another_list = [10, 20, 30, 40]
print(my_list + another_list)

#in above case no new list got created
new_list = my_list + another_list
print(new_list)

# if you use append to append the list it will not merge it will append the list at last inded
my_list.append(another_list)
print(my_list)
# result is [6, 5, 4, 3, 2, [10, 20, 30, 40]]

# Assignment
my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1,2,3,4,5]

#Expected result = ['d','b','a',3,2,1]

my_list.sort()
my_list.reverse()
first_list = my_list[2:]
another_list.sort()
another_list.reverse()
second_list = another_list[2:]
print(first_list + second_list)


## Accessing elements in Nested Lists
my_list = ['a','b','c',1,2,3,['apple', 'orange', 'banana'], 'd']
# print banana
extracted_list = my_list[6][2]
print(extracted_list)

my_list = ['a','b','c',1,2,3,['apple', 'orange', ['john', 'robert'],'banana'], 'd']
# extract rober
extracted_list = my_list[6][2][1]
print(extracted_list)

my_list[6][2][1] = "Joe"
print(my_list)

# Finding index position in Lists and Counting Duplicates
