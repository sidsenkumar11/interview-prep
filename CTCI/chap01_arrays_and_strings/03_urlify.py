"""
Solution:

Swap letters, working right to left.

Note: Don't use string splicing! Strings in python are immutable; splicing actually creates a new string and is inefficient.

Instead, just convert the string to a list in the beginning, and work on the character array. Then finally join the string together at the end.

"""
def urlify(string, length):

    # Convert to char array for efficiency
    string = list(string)

    # Calculate number of spaces to replace in string
    num_spaces = (len(string) - length) // 2

    # Calculate num chars to the left to swap with
    offset = num_spaces * 2

    # Swap from right of string to left
    i = len(string) - 1
    while i > 0:
        if string[i-offset] == ' ':
            string[i]   = '0'
            string[i-1] = '2'
            string[i-2] = '%'
            offset -= 2
            i -= 3
        else:
            string[i] = string[i-offset]
            i -= 1

        if offset == 0 or i-offset < 0:
            break

    # Reform string before returning
    return ''.join(string)

if __name__ == '__main__':
    tests = [('Mr John Smith    ' , 13),
             ('ab cd  '           ,  5),
             ('ab cd efg    '     ,  9),
             ('ab cd ef gh      ' , 11),
             ('a'                 ,  1),
             ('a   '              ,  2),
             (' a  '              ,  2)]
    results = list(map(lambda t: urlify(*t), tests))
    print(*results, sep='\n')
