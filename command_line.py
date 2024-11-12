import sys
import convert
import keyboard
from convert import str_to_float


#Task 3
#Write a program (i.e., include the "main" check from the prior Task) that processes the command-line arguments (available in sys.argv after importing the sys module) by converting each into a float (skipping any that cannot be converted), adding them all together, and then printing the sum.

def main():
    arguments = sys.argv[1:]
    numbers_list = []
    for argument in arguments:
        number = str_to_float(argument)
        if number != None:
            numbers_list.append(number)
    total_sum = sum(numbers_list)
    print(f"the sum of numbers is: {total_sum}")
if __name__ == '__main__':
    main()

