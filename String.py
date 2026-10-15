#multiline string

multiline_string='''This is a multiline string
This is a multiline string
This is a multiline string
This is a multiline string'''

print(multiline_string)

#string slicing[start:stop:step]
string="Python programming"
print(string[0:6])
print(string[::2])
print(string[::-1])

print(len(string))
print('o' in string)

print(string.find('r'))
print(string.index('r'))

#more string methods
string1="Python Programming"
print(string1.upper())
print(string1.lower())
print(string1.capitalize())
print(string1.title())
#more about slicing
string2="Java Programming"

print(string2[5:1:-1])
print(string2.split())