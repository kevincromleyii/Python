# String data type is used to store text data. It is a sequence of characters enclosed in single quotes or double quotes.
# Literal assignment
first = 'Kevin'
last = 'Cromley'

print(type(first)) 
print(type(first) == str) 
print(isinstance(first, str))

# Concatenation
full_name = first + ' ' + last 
print(full_name)

full_name  += ' II'
print(full_name)    

# Casting a number to a string
decade = str(2002)
print(decade)

statement = "I was born in the year " + decade
print(statement)

# Multiple lines
multi_line = '''
This is a multi-line string.
It is a sequence of characters enclosed in triple quotes.
                              Testing
'''
print(multi_line)

# Escaping special characters
sentence = 'I\'m learning Python!    \tTesting\nTesting'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

message = "Part 1 of message "
message += "Part 2 of message"
print(message) # Part 1 of message Part 2 of message because of string concatenation