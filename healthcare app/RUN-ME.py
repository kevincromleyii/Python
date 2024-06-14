import sys


print('') # Print an empty line         
print("********************")
print("*                  *")
print("*    Welcome!      *")
print("*                  *")
print("********************")


name = 'Kevin' 
print('Hello, ' + name + '!') # Print a greeting message
print('') # Print an empty line

input('Press Enter to continue') 
import healthcare # Import the healthcare module

x = input("How did you like our program? Rate from 1-5: ")

if x == '5':
    print("Thank you for your feedback!")
elif x < 4:
    print("We are sorry to hear that. We will try to improve our program.")
else:
    print('That is an invalid response')

