## Debugging

Debugging is the process of identifying, analyzing, and fixing errors or issues (commonly known as "bugs") in a computer program. It involves carefully inspecting the code to ensure that it works as expected and correcting any logical, syntactical, or runtime errors that might cause unexpected behavior or crashes.

<https://youtu.be/b4p-SBjHh28?feature=shared>

<https://youtu.be/7qZBwhSlfOo?feature=shared>


1. The program calculates the sum of integers in a given range. Run the program in debug mode and execute all of its statements step by step. Observe how the values ​​of variables change as the program executes subsequent statements.

    ```python
    ###
    # Calculates the sum of numbers from min_value to max_value
    #
    total = 0
    min_value = 1
    max_value = 5
    number = min_value

    while number <= max_value:
        total = total + number
        number = number + 1

    print(f'The sum of the numbers from {min_value} to {max_value} is {total}')
    ```

1. The program checks what the temperature is and suggests an action depending on the temperature. Unfortunately, the advice does not match the temperature. Modify the program so that it works correctly. Use debugging mode to follow the program's statements step by step.

    ```python
    temperature = 35  # In Celsius

    if temperature > 10:
        print("It's a bit chilly. You might need a jacket.")
    elif temperature > 20:
        print("The weather is nice. How about a walk?")
    elif temperature > 30:
        print("It's hot outside. Stay hydrated!")
    else:
        print("It's cold! Stay indoors or bundle up!")

    print('I hope I helped somehow.')
    ```

1. The program calculates the factorial of a number, but due to a logical error, it multiplies by 0. Modify the program so that it works correctly. Use debugging mode to follow the program's statements step by step.

    ```python
    n = 5
    result = 1 # calculate the factorial for this value

    for i in range(n):
        result *= i

    print(f"Factorial of {n} is:", result)  # Output is incorrect
    ```

1. The program counts the number of vowels, but the count isn't updated correctly. Modify the program so that it works correctly. Use debugging mode to follow the program's statements step by step.

    ```python
    sentence = "hello universe"
    vowels = "aeiou"
    count = 0

    for char in sentence:
        if char in vowels:
            count = count

    print("Vowel count:", count)  # Output is incorrect
    ```

