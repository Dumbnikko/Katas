# DATA TYPES
# str - string
# bool - boolean
# int - integer
# float
# list

# CASTING
# str + int = runtime exception


# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>
#
# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass
#
# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal
# = -> is a designation

"""
  PRACTICE: print each letter in a given string
"""

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input)
"""

"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""

text_value = 'some input'


def search_string(search, text_input):
    result = False
    for character in text_input:
        if character == search:
            result = True
    print(result)


# implement function here


search_string('a', text_value)
search_string('s', text_value)
search_string('S', text_value)
