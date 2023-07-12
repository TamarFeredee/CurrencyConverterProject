from coins import USD, ILS

# Currency converter project:
# Program will convert currency between USD (United States Dollars) and ILS (Israeli Shekel)

global final_result
my_list = []
global file


# Second screen (Choice Screen)
def get_user_value():
    global final_result
    user_choice = input('Please choose an option (1/2): \n1.Dollars to Shekels \n2.Shekels to Dollars \n')
    if user_choice == '1':
        value_to_convert = float(input('Please enter an amount to convert \n'))
        usd = USD()
        final_result = usd.calculate(value_to_convert)
        print("Results is: ", value_to_convert, "Dollars = ", final_result, "Shekels")
    elif user_choice == '2':
        value_to_convert = float(input('Please enter an amount to convert \n'))
        ils = ILS()
        final_result = ils.calculate(value_to_convert)
        print("Results is: ", value_to_convert, "Shekels = ", final_result, "Dollars")
    else:
        print('Invalid Choice, please try again \n')
        get_user_value()
    return final_result


# Third screen (Result screen) + start over (Choice Option)
def start_over():
    user_choice = input('Start over Y / N: \n')
    if user_choice == 'Y':
        get_user_value()
    elif user_choice == 'N':
        end_screen()
    else:
        print('Invalid Choice, please try again \n')
        start_over()


# Fourth Screen (End Screen)
def end_screen():
    global file
    print('Thanks for using our currency converter \n')
    try:
        file = open('/Users/tamarferede/PycharmProjects/firstPoetryPythonProject/results.txt', 'a')
    except (FileNotFoundError, IOError):
        print("File Not Found / Wrong file or file path")

    integer = save_result_to_list()
    file.write(str(integer))
    print_final_results()


# Print the final results:
def print_final_results():
    global file
    try:
        file = open('/Users/tamarferede/PycharmProjects/firstPoetryPythonProject/results.txt', 'r')
    except (FileNotFoundError, IOError):
        print("File Not Found / Wrong file or file path")

    content = file.read()
    print("All the results: ", content)
    file.close()


# Saving the result to list
def save_result_to_list():
    my_list.append(final_result)
    print(my_list)
    return my_list


# The main function to run
def main():
    # First screen (Welcome Screen)
    print('Welcome to currency converter')
    # Calling the methods that I already created in order to run the program
    get_user_value()
    start_over()


main()
