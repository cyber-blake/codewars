# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.


def is_prime(num):
    for x in range(2, num):
        # print(f"{num} % {x} = {num%x}")
        if num % x == 0:
            return False
        else:
            return True


print(is_prime(73))
# todo не учитывает 0, 1, 2; 9, 45 - кратные другим, и отрицательные
