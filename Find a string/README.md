# HackerRank Problem: Find a String

## Problem Statement

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

### Function Description

Complete the function `count_substring` in the editor below.

#### `count_substring` has the following parameters:
- **string string**: The string to search.
- **string sub_string**: The substring to search for.

### Input Format
The first line of input contains the original string.
The second line contains the substring.

### Constraints
- Each character in the string and the substring is an ASCII character.
- **1 \<= len(string) \<= 200**
- **1 \<= len(sub_string) \<= len(string)**

### Output Format
Print the integer number indicating the total number of occurrences of the substring in the original string.

### Sample Input 0
```
ABCDCDC
CDC
```

### Sample Output 0
```
2
```

### Explanation 0
The substring `CDC` appears twice in the string `ABCDCDC`:
- First occurrence: starting at index 2
- Second occurrence: starting at index 4
