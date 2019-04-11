"""
----------
Method 1
----------

Create a hash table and store each character. Check if the character appears again.

Time:  O(n)
Space: O(n)

Sets use hashtable as the underlying data structure.
- On average we have O(1) membership check and O(1) insertion.
"""
def is_unique_one(string):
    seen = set()
    for x in string:
        if x in seen:
            return False
        seen.add(x)
    return True

"""
-----------
Method 2
----------

Don't use extra data structures by using bit vectors.
Each bit in the bit vector represents a "seen" value.
- 0 means seen, 1 means unseen.
- Keep a bit for all 256 possible values.
- Use XOR to clear the bit if it's seen.
- Use AND to check if the bit is still set.

Time:  O(n)
Space: O(1)

Note that we kind of cheat here; internally Python represents
the large integer using an array of 30-bit or 15-bit numbers.
But if we wanted to, we could split the vector into several ints ourselves.
"""
def is_unique_two(string):
    vector = (1 << 256) - 1 # 256 '1' bits
    for x in string:
        if (1 << ord(x)) & vector:
            vector ^= 1 << ord(x)
        else:
            return False
    return True

"""
---------
Method 3
---------

Essentially do the same thing as Method 2, but simpler. 
Also note small optimization: a string of length > 256 must have repeats.
"""
def is_unique_three(string):

    if len(string) > 256:
        return False

    seen = [False] * 256
    for x in string:
        if seen[ord(x)]:
            return False
        seen[ord(x)] = True
    return True

if __name__ == '__main__':

    """
    Quick/easy way to test multiple inputs.
    - map(func, list)
    - map returns a generator that generates the results of
      calling func on each element of the list
    - list() creates a list of results
    - *result unpacks the list, and print() prints each argument separated by a space by default
    """
    tests = ["", "a", "abcd", "abcda"]
    results = list(map(lambda t: is_unique_one(t), tests))
    print(*results, sep='\n')
    print('---------------------')
    results = list(map(lambda t: is_unique_two(t), tests))
    print(*results, sep='\n')
    print('---------------------')
    results = list(map(lambda t: is_unique_three(t), tests))
    print(*results, sep='\n')
