# HackerRank Problem: Python Lists

## Problem Statement

Consider a list (list = []). You can perform the following commands:

1. **insert i e**: Insert integer **e** at position **i**.
2. **print**: Print the list.
3. **remove e**: Delete the first occurrence of integer **e**.
4. **append e**: Insert integer **e** at the end of the list.
5. **sort**: Sort the list.
6. **pop**: Pop the last element from the list.
7. **reverse**: Reverse the list.

Initialize your list and read in the value of **n** followed by **n** lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

### Input Format
- The first line contains an integer, **n**, denoting the number of commands.
- The next **n** lines contain one of the commands described above.

### Constraints
- The elements added to the list must be integers.

### Output Format
For every **print** command, output the list on a new line.

### Sample Input 0
```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

### Sample Output 0
```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

### Explanation 0
- **insert 0 5**: Insert 5 at index 0 → [5]
- **insert 1 10**: Insert 10 at index 1 → [5, 10]
- **insert 0 6**: Insert 6 at index 0 → [6, 5, 10]
- **print**: Print the list → [6, 5, 10]
- **remove 6**: Remove the first occurrence of 6 → [5, 10]
- **append 9**: Append 9 to the list → [5, 10, 9]
- **append 1**: Append 1 to the list → [5, 10, 9, 1]
- **sort**: Sort the list → [1, 5, 9, 10]
- **print**: Print the list → [1, 5, 9, 10]
- **pop**: Pop the last element → [1, 5, 9]
- **reverse**: Reverse the list → [9, 5, 1]
- **print**: Print the list → [9, 5, 1]
