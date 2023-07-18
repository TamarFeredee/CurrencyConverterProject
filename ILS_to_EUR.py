from coins import USD, EUR

global final_result
my_list = []
global file


# Second screen (Choice Screen)
def get_user_value():
    global final_result
    user_choice = input('Please choose an option (1/2): \n1.Shekels to EUR \n2.Dollars to Shekels \n')
    if user_choice == '1':
        value_to_convert = float(input('Please enter an amount to convert \n'))
        eur = EUR()
        final_result = eur.calculate(value_to_convert)
        print("Results is: ", value_to_convert, "Eur = ", final_result, "Shekels")
    elif user_choice == '2':
        value_to_convert = float(input('Please enter an amount to convert \n'))
        usd = USD()
        final_result = usd.calculate(value_to_convert)
        print("Results is: ", value_to_convert, "Dollars = ", final_result, "Shekels")
    else:
        print('Invalid Choice, please try again \n')
        get_user_value()
    return final_result


# The main function to run
def main():
    # First screen (Welcome Screen)
    print('Welcome to currency converter')
    # Calling the methods that I already created in order to run the program
    get_user_value()


main()
