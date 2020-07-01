# Author: Mark Mendez
# Date: 6/30/2020
# Description: generates binary search fractions but doesn't alternate halves

# generate denominators in outer loop.
# Each iteration makes a fraction that can be used as a multiplier for .length() in binary search
denominator = 1
for fraction in range(1, 10):  # range denotes depth; how many
    denominator *= 2

    # generate numerators in inner loop
    numerator = 1
    while numerator < denominator:
        multiplier = numerator / denominator  # generates all the multipliers but doesn't do anything with them
        print(numerator, '/', denominator, '\tmultiplier', multiplier)
        numerator += 2  # every odd number is the previous + 2
