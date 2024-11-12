import convert
#Task 2
#function gather_numbers() will not take any arguments. It will return a
#list of float values. The function must read a series of numbers from
# the user by prompting and reading each number from the keyboard
# (using the input() function). It is expected that only a single
# number is entered each time, but the user may mistype something.
# As such, your solution should use the str_to_float function from
# the prior task. Any input that cannot be converted will be skipped;
# as such, the returned list will contain only the properly converted
# floats. The function must continue to take input until the user types "done".

def gather_numbers()-> list[float]:
    number_list = []
    while True:
        user_input = input("enter a number or type 'done' to stop")
        user_input = user_input.strip()
        if user_input.lower() == 'done':
            break
        else:
            number = convert.str_to_float(user_input)
            if number != None:
                number_list.append(number)
    return number_list

if __name__ == "__main__":
    numbers = gather_numbers()
    print(f"the list of the numbers is: {numbers}")

