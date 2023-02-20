import random

def most_sig_bit(n: int = 0):
    # Find the largest power of 2 that is less or equal to N
    while n & n-1:
        n = n & n-1
    return n


def sig_bit_their_way(n: int = 0):
    for i in range(4):
        n = n | (n >> (2**i))
    return (n+1) >> 1


error_count = 0
test_size = 500000
power_list = [i for i in range(5, 11)]
random_list = [random.random() for i in range(test_size)]
for power in power_list:
    for rando in random_list:
        num = int(rando * 10**power)
        sure_way = most_sig_bit(num)
        their_way = sig_bit_their_way(num)
        if sure_way != their_way:
            error_count += 1
            # print("Power: ", power)
            # print("Number: ", num)
            # print(" Sure way: ", my_way)
            # print("Their way: ", their_way)
            # print("Not equal")
            # print("-----------\n")
    print("Numbers >= ", 10**power)
    print(f"Errors: {error_count}/{test_size}")
    print("Error Percent: ", (error_count / test_size))
    print("----------\n")
total_tests = test_size * len(power_list)
print(f"Errors across all tests: {error_count}/{total_tests}")
print("Error Percent: ", (error_count / total_tests))




