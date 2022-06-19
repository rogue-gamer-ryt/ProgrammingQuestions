"""
Write a program which takes as input a phone number, specified as a string of digits, and returns
all possible character sequences that correspond to the phone number. The cell phone keypad is
specified by a mapping that takes a digit and returns the corresponding set of characters. The
character sequences do not have to be legal words or phrases.
"""

MAPPING = ['0','1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# Time complexity - O(n * 4**n)
def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonics
            # (We add a copy since subsequent calls modify partial_mnemonic)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # Try all possible characters for this digit
            for c in MAPPING[int(phone_number[digit])]:
                print(partial_mnemonic)
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

assert phone_mnemonic("23") == ["AD","AE","AF","BD","BE","BF","CD","CE","CF"]