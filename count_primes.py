def is_prime(n: int) -> bool:
    count = 2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1
        if count > 2:
            return False
    return True


def get_prime_count(num: int) -> int:
    count = 0
    for num in range(2, num):
        if is_prime(num):
            count += 1
    return count


try:
    number = int(input("Enter a number to get prime count less than itself : "))
    print(f"The count of primes less than {number} is : ", get_prime_count(number))
except ValueError:
    print("Invalid input. Enter only integer")
