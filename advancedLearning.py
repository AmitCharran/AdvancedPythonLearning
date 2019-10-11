# Generator or generator functions
from symbol import decorator

print('\n\nGenerator Functions -- line 2')
print('Generator Functions are basically iterators but with a different approach\n'
      'They are a simple function with returns,"yields", iterable set of items\n')
import random as rn
def lottery():
    for i in range(6):
        yield rn.randint(1, 40)
    yield rn.randint(1,15)


for number in lottery():
    print("And the next number is ... %d" % number)

a2 = 1
b2 = 2
a2, b2 = b2, a2
print(a2, b2)  # simultaneously switch the values of a and b


def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


import types  # need to import types to get the function types.GeneratorType
if type(fib()) == types.GeneratorType:
    print('print function is a Generator')


counter = 0
for n in fib():
    print(n),
    counter += 1
    if counter == 10:
        break


# List Comprehension
print('\n\nList Comprehension -- line 42')
print('List Comprehension creates new lists based on another list, in a single, readable line')

sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()  # This functions splits words in a string
words_length = []  # Creates empty array
for word in words:
    if word != 'the':
        words_length.append(len(word))
print(words)
print(words_length)

print('\nNow do this using List Comprehension')
sentence2 = 'the quick brown fox jumps over the lazy dog'
words2 = sentence2.split()
words_length2 = [len(word) for word in words2 if word != 'the']
# for above ^ :to this array add in the length of word: for word in words2: if that word != 'the'
print(words2)
print(words_length2)

# Second Example
number = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newList = [num for num in number if num >= 0]
print('\nSecond Example\n' + str(newList))

# Multiple Function Arguments
print('\n\nMultiple Function Arguments -- line 68')
print("So it's like overloaded function but it's all in one function\n"
      "So a function can have one parameter and the rest of the parameter\n"
      "\"the rest\" can be however many parameters you want")

# Here is an example of a normal function
def foo(first, second, third):
    print('First %s ' % first)
    print('Second %s ' % second)
    print('Third %s ' % third)

print("\nExample of normal function")
foo('this','that','other')

# Example of a Multiple Function Argument
def foo2(first, second, third, *theRest):
    print('First %s ' % first)
    print('Second %s ' % second)
    print('Third %s ' % third)
    print('The Rest % s' % list(theRest))

print("\nExample with Multiple Function Argument")
foo2('this','that','other','another','this one too', 'also this one')

print('\nIt is possible to send function arguments by keyword using syntax **'
      '\nSO THE ORDER OF THE ARGUMENT DOES NOT MATTER -- line 93')
def bar(first, second, third, **options):
    if options.get("actions") == 'sum':
        print('the sum is %d' % (first + second + third))
    if options.get("number") == "first":
        return first;

# the bar function receives three arguments, if additional "action" function is received,
# and it instructs on 'sum', then the sum will be printed.
# Alternatively the function is also instructed to return the first parameter
# IFF "number" parameter instructs 'first'

result = bar(1, 2 ,3, actions = 'sum', number = 'first')
print(result)
print('Need to find other practice on this, I do not fully understand')

# Regular Expression
print('\n\nRegular Expresssions -- line 110')
print('Regular Expressions are tools for matching patterns in text\n'
      'Sometimes shortened as regexp, regex, re(This is the one python uses)')
print('\nAn example of regex is r"^(From|To|Cc).*?python-list@python.org"'
      '\nthe caret "^" matches text at the beginning of a line. '
      '\nThe following group, the part with "(From|To|Cc)" means that the line'
      ' has to start with one of the words that are seperated by the pipe "|"'
      '\n"|" <- that is the OR operator, and the regex will match if the line'
      'starts with any of the words in the group'
      '\n".*?" <- that means to ungreedily match any number of characters, except'
      ' the newline "\\n" character'
      '\nThe un-greedy part means to match as few repetitions as possible.'
      '\n"." <- that character means any non-newline character'
      '\n"*" <- that means repeat 0 or more times'
      '\n"?" <- that character makes it un-greedy')

print('\nComplete reference of "re" syntax in Python docs '
      '- https://docs.python.org/3/library/re.html#regular-expression-syntax%22RE%20syntax -')

import re
pattern = re.compile(r"\[(on|off)\]")  # In the compile the parameter is a "pattern"
# Exercise: make a regular expression that will match an email

import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com","python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]

    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s." % email)

        elif not your_pattern:
            print("Forgot to enter pattern.")
        else:
            print("Pass")


pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)

print("\nRegular Expressions were not taught well so need to revisit this")

# Exception Handling
print('\n\nException Handling -- line 154')
print("Similar to exception handling in java")

# Example of Exception
def do_stuff_with_number(n):
    print(n),

the_list = (1, 2, 3, 4, 5)
for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError:  # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)

# Not an Example
actor = {"name" : "John Cleese", "rank" : "awesome"}

def get_last_name():
    return actor["name"].split()[1]  # Get the second index when you split the name into 'words'


print('\nDocument with Exception Handling for more details '
      '- https://docs.python.org/3/tutorial/errors.html#handling-exceptions -')


# Sets
print('\n\nSets -- line 180')
print('Sets are a list with no duplicate entries')

#Example
print(set("my name is Eric and Eric is my name".split()))

print('\nYou can also calculate intersection between other sets')
a = set(['Jake', 'John', 'Jill'])
print("Set a = " + str(a))
b = set(['Eric','John'])
print("Set b = " + str(b))

print("\na.intersection(b) = " + str(a.intersection(b)))
print("b.intersection(a) = " + str(b.intersection(a)))

print('\nThere is also the "symmetric_difference" method')
print("a.symmetric_difference(b) = " + str(a.symmetric_difference(b)))
print("b.symmetric_difference(a) = " + str(b.symmetric_difference(a)))

print('\nThere is also a "difference" method')
print("a.difference(b) = " + str(a.difference(b)))
print("b.difference(a) = " + str(b.difference(a)))

print('\n"Union" method')
print("a.union(b) = " + str(a.union(b)))
print("b.union(a) = " + str(b.union(a)))


# Serialization
print('\n\nSerialization - line 209')
print("Serialization is basically to encode and decode JSON")

import json
json_string = json.dumps([1, 2, 3, "a", 'b', 'c'])
print(json.loads(json_string))

print('\npickle is also another serialization method, like JSON')
import pickle
pickled_string = pickle.dumps([1, 2, 3, 'a', 'b', 'c'])
print(pickle.loads(pickled_string))

print('\nAnother JSON example')


def add_employees(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return json.dumps(salaries)


# test code
salaries = '{"Alfred" : 300, "Jane" : 400}'
new_salaries = add_employees(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"]),
print(decoded_salaries["Jane"]),
print(decoded_salaries["Me"]),


#Partial Function
print('\n\n\nPartial Function  -- line 240')
print('Partial function allows one to derive a function with x parameters to a '
      'function with fewer parameters and fixed valued set for the more limited function')

from functools import partial
def multiply(x,y):
        return x*y

#create a new function that multiplies by two
dbl = partial(multiply,2)
print(dbl(4))

def func(u, v, w, x):
    return (u*4) + (v*3) + (w*2) + (x)


p = partial(func, 5, 6, 7)
print(p(8))

# Code Introspection
print('\n\nCode Introspection -- line 260')
print('Code Introspection is the ability to examine classes, functions, and keywords to know'
      ' what they are, what they do, and what they know1')

print('\nSome commands are:'
      '\nhelp() - It is used it to find what other functions do'
      '\ndir()'
      '\nhasattr() - Checks if an object has an attribute'
      '\nid()'
      '\ntype()'
      '\nrepr() - Return string representation of object'
      '\ncallable() - Checks if an object is a callable object (a function)or not.'
      '\nissubclass() - Checks if a specific class is a derived class of another class.'
      '\nisinstance() - Checks if an objects is an instance of a specific class.')

print('\nExample')
# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))


# Closure
print("\n\nClosure -- line 291")
print("Closure is a function object that remembers values in enclosing scope even if"
      " they are not present in memory.")
print("So in a nested function, it can use variables from the outer function\n"
      "But you need to 'call' inner functionat the end of outer function")

def transmit_to_space(message):
    "This is the enclosing function"
    x = 32
    def data_transmitter():
        "The nested function"
        print(message + " " + str(x))

    data_transmitter()

print(transmit_to_space("\nTest message"))

# Another Example
def print_msg(number):
    def printer():
        "Here we are using non-local keyword"
        non_local_num = 3
        print(non_local_num)
    printer()
    print(number)


print_msg(9)

# Another Example
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter


fun2 = transmit_to_space("Praise the Sun!")
fun2()

# Last Example
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

# Decorators
print('\n\nDecorator -- line 343 -- I\'m skipping this...')
print('Decorator allows you to make simple modification to callable objects like functions, methods, and classes.'
      '\nIt takes a function and returns one.')


@decorator
def functions__(arg):
    return "value"


def function(arg):
    return "value"


function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions



def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value