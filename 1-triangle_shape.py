try:
    num = int(input("Enter an odd number: "))  # take input from user
    if num % 2 == 0:
        raise ValueError("Number should be odd!")
    for i in range(num, 0, -2):  # loop to generate pattern
        asterisks = "*" * i
        print(asterisks.center(num + 2))
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Error:", e)
