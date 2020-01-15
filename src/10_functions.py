# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
print(is_even(4))
# Read a number from the keyboard

num = input("Enter a number: ")
num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_evenSay(numberTwo):
    if numberTwo % 2 == 0:
        print('Even!')
    else:
        print('Odd')
        
is_evenSay(num)