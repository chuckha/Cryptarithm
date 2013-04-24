from itertools import permutations
from equation import Words, Numbers, generate_numbers


def solve(*words):
    """Create patterns from words.

    words:    SEND + MORE = MONEY
    patterns: 0123 + 4561 = 45217

    Grab actual numbers from the nums_array and turn those numbers into patterns.

    numbers:  9567 + 1085 = 10652
    patterns: 0123 + 4561 = 45217

    This is a success because the two pattern sets match up.
    """
    words = Words(*words)

    nums_array = [0,1,2,3,4,5,6,7,8,9]
    for perm in permutations(nums_array):
        # patterns stay the same, permutation of numbers changes
        ns = generate_numbers(perm, words.patterns[:-1])
        ns.append(sum(ns))
        numbers = Numbers(*ns)
        if numbers.patterns == words.patterns:
            return numbers.numbers
    return ()
     
if __name__ == '__main__':
    print solve("broo", "klyn", "folk")
