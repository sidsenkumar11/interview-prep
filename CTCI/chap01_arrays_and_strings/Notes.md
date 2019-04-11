# Arrays and Strings

## Hash Table

Normally, hash tables are implemented as a contiguous chunk of memory - one space is allocated for each hashcode. This gives O(1) performance, but could take a lot of space depending on the number of possible hash codes. To save space, we could instead implement the hash table with a balanced binary search tree, so we only allocate space for each hash code that's actually used. This gives us an O(log N) lookup time though, instead of O(1).

## ArrayList & Resizable Arrays

Resizing a dynamic array takes O(n) to copy all the old elements of the backing-array into a new backing-array, but this happens so rarely that insertion is amortized to O(1). In Java, resizing == doubling.

Why is it amortized to O(1)? If we inserted N elements:
    - 1st capacity increase copies 1 element
    - 2nd capacity increase copies 2 elements
    - 3rd capacity increase copies 4 elements
      ...
    - second-to-last capacity increase copies n/4 elements
    - last capacity increase copies n/2 elements

The total number of copies is N/2 + N/4 + N/8 + ... + 4 + 2 + 1 = Just under N
So, inserting N elements takes ~N copies, so each insertion takes O(1) on average.

## StringBuilder

Strings are immutable data types in Java. So appending to a string actually copies all the elements of the old string into a new string, and then appends the new characters to the end of the new string. Appending an x-character string n times takes O(x**n²). Why?
- We copy x characters on first concatenation.
- We copy 2x characters on the second concatenation.
- ...
- We copy nx characters on the nth concatenation.
 The number of character copies in total is  x + 2x + 3x + ... + nx = x (1 + 2 + 3 + ... + n) = x (n(n+1)/2) = x(n²).

By using Java's StringBuilder, we basically have a mutable String. It creates a resizable array for a string and only copies when resizing the array.

Example:
```
StringBuilder sentence = new StringBuilder();
for (String w : words) {
    sentence.append(w);
}
System.out.println(sentence.toString());
```

