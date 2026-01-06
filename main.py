
def main():

    # Task 1
    pet_type = 'dog'
    pet_name = 'daisy'

    print(f'I have a {pet_type} and her name is {pet_name}.')

    # Task 2 (Inputs and manipulate data within print statements)
    first_name = input('Enter your first name: ')
    age = int(input('Enter your current age: '))
    yearly_savings = int(input('Enter your yearly savings: '))
    print(f'Hello {first_name}! You are currently {age} years old.')
    print(f'In 10 years, you will be {age + 10} years old.')
    print (f'If you save {yearly_savings} each year, in 5 years you will have saved {yearly_savings * 5}.')
    print(f'Your average monthly savings is {yearly_savings / 12}')

    # Task 3 (31 days, 24 hours in a day, 60 minutes in an hour, 60 seconds in a minute)
    print(f'The Number of seconds in January is {31 * 24 * 60 * 60}')

    # Task 4
    eggs = int(input('Enter your number of eggs: '))
    print(f'This makes {eggs//12} dozen eggs with {eggs%12} left over.')

if __name__ == '__main__':
    main()