def steps(number):
    steps_counter = 0

    if number < 1 or number != int(number):
        raise ValueError("Not positive integer")

    # number is even:
    while number != 1:

        if number % 2 == 0:
            number = number // 2
            steps_counter += 1
        # number is odd:
        else:
            number = number * 3 + 1
            steps_counter += 1

    return steps_counter

