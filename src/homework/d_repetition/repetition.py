def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    sum_odds = 0
    current_num = 1
    while current_num <= num:
        sum_odds += current_num
        current_num += 2  # Skip to the next odd number
    return sum_odds
