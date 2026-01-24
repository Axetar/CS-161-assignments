
def main():
    # Task 1 - ask for name
    print ('Hello ' + input('what is your name? '))

    # Task 2 - it would've been an error as it was seen as a string but use int() converts it into an int
    age = int(input("whats your age? "))
    print(age + 5)

    # Task 3
    yrs = int(input("How many years do you want to add? "))
    print('In ' + str(yrs) + ' you will be ' + str(age+yrs) + " years old.")

    # Task 4 / 5
    hours = float(input("Enter the number of hours worked: "))
    wage = float(input("Enter your hourly wage, without the $: "))

    # Calc weekly pay and annual
    weekly_pay = hours * wage
    annual_pay = weekly_pay * 50

    # Display the result
    print("Your gross pay this week is $ " + str(weekly_pay) +
          "\nYour estimated annual gross pay will be $ " + str(int(annual_pay)))

if __name__ == '__main__':
    main()
