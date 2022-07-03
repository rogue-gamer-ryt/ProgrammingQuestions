"""
The Collatz conjecture is the following: Take any natural number. If it is odd, triple it and add one;
if it is even, halve it. Repeat the process indefinitely. No matter what number you begin with, you
will eventually arrive at 1.

Test the Collatz conjecture for the first n positive integers.
"""


def test_collatz_conjecture(n):
    verified_numbers = set()

    # hypothesis holds trivally for 1
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # This would prove that its in a loop and we will never reach 1
                return False
            sequence.add(test_i)

            if test_i % 2: # if the number is odd
                if test_i in verified_numbers:
                    break
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //=2
    return True


assert test_collatz_conjecture(10) == True