#_str = 'test'
#_str2 = 'toast'
#_str3 = '{_str2} test'.format(_str2=_str2)
#_str4 = f(_str2)

#casting
''''
#output = '1' + 1
'''
output = int('1') + 1
output2 = '1' + str(1)

print (output)
print (output2)


#boul

print(bool(0))
print(bool(1))
print(bool(.1))
print(bool(None))
print(bool())
print(bool('false'))

#list

_list = ['alex', 'grande', 'sara', 'danie', 'laura', 'jen']

print(_list)



"""
practisse: create a funcion thattakes an input, than prints 
each character of the input
"""

def print_character(input):
    for character in input:
        print(character)
print_character('batman')

"""
practice: create a funciton that takes 2 inputs,
then prints True/False whether or not the first input
is contained within the second input
"""

#== compares

def search_character(search, find):
    for character in find:
        if character == search:
            print(True)
search_character('a', 'purple')
