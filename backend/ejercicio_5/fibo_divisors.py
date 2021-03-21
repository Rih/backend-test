import itertools


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


def get_max_divisors(dp, max_length):
    divisors = [1]
    current_max = 0
    fib_value = '0'
    i = 0
    if max_length < 3:
        return max_length
    i_iter = iter(itertools.count(start=2, step=2))  # infinite iterator
    while current_max < max_length:
        i = next(i_iter)
        n, dp = fibo(i, dp)
        nth_fib = str(i)
        fib_value = str(n)
        divisors = [1]  # default divisor to all numbers
        # check all divisors
        for d in range(2, dp[nth_fib] + 1):
            if dp[nth_fib] % d == 0:
                divisors.append(d)
        total_divisors = len(divisors)
        # check stop condition
        if total_divisors >= current_max:
            current_max = total_divisors
    print(f'\n{nth_fib}th fibo found:  with fib value: {fib_value} with {len(divisors)} divisors')
    print(f'\nAll divisors are: {divisors}')
    return nth_fib, fib_value


if __name__ == '__main__':
    # omit 0 by definition now
    dp = {'1': 1, '2': 1}
    exit_condition = "!e"
    max_divisor = 100
    print(f"\n*********************************************")
    print(f"Executing exercise 5. ")
    print(f"The result will be a tuple of 2 integers: ")
    print(f"The first will be a nth fibonacci position")
    print(f"The second will be the fibonacci according to the nth position")
    print(f"\nExecuting algorithm with input: \"{max_divisor}\"")
    print("Please wait...")
    nth, fib = get_max_divisors(dp, max_divisor)
    str_input = input(f"Enter other example at your OWN risk, recommended less than 2000 :) (Type \"{exit_condition}\" to exit): ")
    while str_input != exit_condition:
        nth, fib = get_max_divisors(dp, int(str_input))
        str_input = input(f"Enter other example at your OWN risk, recommended less than 2000 :) (Type \"{exit_condition}\" to exit): ")
    print("Finish.")


