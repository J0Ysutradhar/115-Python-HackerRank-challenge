# HackerRank Problem: Python Tuples1

## Problem Statement

Given an integer, **n**, and **n** space-separated integers as input, create a tuple, **t**, of those **n** integers. Then compute and print the hash value of the tuple.

### Input Format
- The first line contains an integer, **n**, denoting the number of elements in the tuple.
- The second line contains **n** space-separated integers describing the elements in the tuple.

### Output Format
Print the hash value of the tuple.

### Constraints
- **2 \<= n \<= 100**
- Each integer will be in the range **-10^9 \<= a[i] \<= 10^9**

### Sample Input 0
```
2
1 2
```

### Sample Output 0
```
3713081631934410656
```

### Explanation 0
- The tuple **t** is created as `(1, 2)`.
- The `hash()` function computes the hash value of the tuple, which is outputted as `3713081631934410656` in this case.

### Note
The `hash()` function is used to return the hash value of an object if it has one. This function is supported for tuples in Python.
