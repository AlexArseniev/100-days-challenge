# Write your code below this line ๐
def prime_checker(number):
    if number == 2 or number == 3:
        print("It's a prime number.")
        return
    if number % 2 == 0 or number % 3 == 0 or number == 1:
        print("It's not a prime number.")
        return
    print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)