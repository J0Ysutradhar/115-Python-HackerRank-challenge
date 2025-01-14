# HackerRank Problem: String Split and Join

## Problem Statement

You are given a string. Split the string on a "space" delimiter and join using a hyphen (`-`).

### Input Format
A single line of input containing the string, **S**.

### Constraints
- **0 \<= len(S) \<= 1000**

### Output Format
Print the modified string where words are joined with a hyphen.

### Sample Input 0
```
this is a string
```

### Sample Output 0
```
this-is-a-string
```

### Explanation 0
The string is split into words using a space as the delimiter. Then, the words are joined together using a hyphen (`-`) as the delimiter to produce the output:
```
this-is-a-string
```

### Note
- Use Python's built-in string methods `.split()` and `.join()` for an efficient solution.
