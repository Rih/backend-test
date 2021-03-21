import itertools
import time
import math
import random


def fibo(n, dp):
    if n == 0 or n == 1:
        return n, dp
    if dp.get(str(n - 1)) and dp.get(str(n - 2)):
        dp[str(n)] = dp[str(n - 1)] + dp[str(n - 2)]
    else:
        n_1, dp = fibo(n - 1, dp)
        n_2, dp = fibo(n - 2, dp)
        dp[str(n)] = n_1 + n_2
    return dp[str(n)], dp


def get_delivery_days(dp, distance):
    ith = math.ceil(distance / 100.0)
    if distance < 100.0:
        return dp, 0
    n, dp = fibo(ith - 1, dp)
    nth_fib = str(ith)
    return dp, n


if __name__ == '__main__':
    exit_condition = "!e"
    dp = {'0': 0, '1': 1}
    print(f"\n*********************************************")
    print(f"Executing exercise 6. ")
    print(f"The result will be a dictionary and an integer")
    print(f"The first will be a store with previous values")
    print(f"The second will be the value asked for,")
    print("that means the estimate days for delivery.")
    examples = input("Please enter a number ")
    print("It'll create random examples all between [0, 2000] km: ")
    time.sleep(5)
    distances = [random.randint(0, 2000) for x in range(int(examples))]
    for dist in distances:
        print(f"\nExecuting algorithm with input: \"{dist}\" km")
        dp, estimate_days = get_delivery_days(dp, dist)
        print(f'For distance: {dist} km is {estimate_days} days')

    str_input = input(f"Enter other example from 0 to 2000 (Type \"{exit_condition}\" to exit): ")
    while str_input != exit_condition:
        dp, estimate_days = get_delivery_days(dp, int(str_input))
        print(f'For distance: {str_input} km is {estimate_days} days')
        str_input = input(f"Enter other example from 0, 2000 (Type \"{exit_condition}\" to exit): ")
    print("Finish.")


