# Printing a Welcome message
print('Welcome to My Calculator!')

# Print instructions on how to use the calculator
print('''Use This Calculator for simple calculations.
Use '+' to add\n
Use '-' to subtract\n
Use '/' to devide\n
Use '*' to multiply\n
Use '%' for modulus remainder of the division of left operand by the right\n
Use '**' for exponent left operand raised to the power of the right\n
Use '//' for floor division that results into whole number adjusted to the left in the number line\n
Example input: 2+2 
output: 4''')
user_input = ''

# Using a while loop to continue looping through the code until the user enters '0'
while user_input != "0":
    # using eval() function to calculate the users input
    print(eval(f'{input("Enter Your calculation: ")}'))
    # Asking the user to enter either '0' to exit or '1' to continue
    user_input = input("Enter 0 to quit and 1 to continue: ")
    if user_input == '1':
        continue
    # If user does not enter a valid option the program will exit
    else:
        print('Invalid Option, Exiting Program...')
        break
# If the user enters '0' a goodbye message will be printed and it will exit the program
if user_input == '0':
    print("Thanks for using my calculator \n GoodBye!")