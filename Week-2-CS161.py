
def main():

    # Task 1
    x = 31
    print(x, bin(x), hex(x))

    # Task 2
    # x = 1.825
    # You get an error that a float cannot be seen as an int
    # This make sense as we establish x as an int making it work with bin and hex, but bin and hex cannot take a float as an input leading to an error

    x = 18
    print(x, bin(x), hex(x))

    # Task 3
    y = 0b1011
    z = 0xA3
    print(y, z) # Prints out the literal number associated with the binary/hex value

    # Task 4
    w = x + y + z
    print('the sum is ', w) # Due to python being a high level language it's able to intepret the different variables and add them together

    #-------
    # Section 2
    #-------

    # Task 1
    original_size = 240

    dictionary_size = 25

    compressed_text_size = 148

    compressed_percentage = (1 - ((compressed_text_size + dictionary_size) / original_size)) * 100

    print('Compressed text size:', compressed_text_size, 'characters')
    print('     Dictionary size:', dictionary_size, 'characters')

    print('               Total:', dictionary_size + compressed_text_size, 'characters')
    print('  Original text size:', original_size, 'characters')
    print('          Compressed:', str(round(compressed_percentage, 2)) + '%')


if __name__ == '__main__':
    main()