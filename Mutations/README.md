# HackerRank Problem: Python Mutations1

## Problem Statement

You are given a string, and you need to modify it according to the given instructions. Write a function that performs the following operation:

- Replace the character at a specified index in the string with another character.

### Function Description

Complete the function `mutate_string` in the editor below.

#### `mutate_string` has the following parameters:
- **string s**: The original string.
- **int position**: The zero-based index of the character to replace.
- **string character**: The new character to insert.

### Input Format
The first line contains the original string, **s**.
The second line contains two values:
- An integer, **position**, the index to replace.
- A string, **character**, the new character to insert.

### Constraints
- **1 \<= len(s) \<= 1000**
- The input string **s** contains only alphanumeric characters.

### Output Format
Return the modified string.

### Sample Input 0
```
abracadabra
5 k
```

### Sample Output 0
```
abrackdabra
```

### Explanation 0
The string **s** is `abracadabra`. We replace the character at index 5 (0-based) with `k`. The modified string is `abrackdabra`.
