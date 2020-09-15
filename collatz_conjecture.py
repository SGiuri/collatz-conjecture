def steps(number):
    steps_counter = 0

    print(number)
    # number is even:
    while number != 1:

        if number % 2 == 1:
            number = number / 2
            steps_counter += 1
        # number is odd:
        else:
            number = number * 3 + 1
            steps_counter += 1

        print(number)
    return steps_counter
