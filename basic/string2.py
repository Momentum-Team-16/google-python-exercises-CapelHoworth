#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
MY_CONSTANT = "This is the thing I want to be available everywhere"
# This is how we do global scope in Python. Available anywhere in the program
# Convention to write constants in ALL CAPS


def verbing(s):
  if len(s) < 3:
    return s
  elif s.endswith("ing"):
    return s + "ly"
  else:
     return s + "ing"


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


def not_bad(s):
  """new_string = ""
  if s.find("not") < s.find("bad"):
    new_string = s.replace("good")
  return new_string"""
  pass


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# make a helper function


def half_length(string):
  if len(string) % 2 == 0:
    return int(len(string) / 2)
  else:
    return int(len(string) / 2) + 1


def slice_front(string):
  return string[:half_length(string)]


def slice_back(string):
  return string[half_length(string):]


def front_back(a, b):
  a_front = slice_front(a)
  a_back = slice_back(a)
  b_front = slice_front(b)
  b_back = slice_back(b)
  return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swimming'), 'swimmingly')
  test(verbing('do'), 'do')

  print
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
  main()
