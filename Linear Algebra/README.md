# HackerRank Problem: Linear Algebra

## Problem Statement1

You are given a square matrix **A** with dimensions **N x N**. Your task is to compute the determinant of **A**.

### Input Format
- The first line contains the integer **N**, the size of the square matrix **A**.
- The next **N** lines contain the **N** space-separated elements of row **A[i]**.

### Output Format
Print the determinant of **A**.

### Constraints
- **2 \<= N \<= 10**
- Elements of the matrix are floats with absolute value <= 100.

### Note
- Round the result to 2 decimal places.
- Use the `numpy.linalg.det` function to compute the determinant.

### Sample Input 0
```
2
1.1 1.1
1.1 1.1
```

### Sample Output 0
```
0.00
```

### Explanation 0
The determinant of the given matrix is calculated as:
```
| 1.1  1.1 |
| 1.1  1.1 |
```
Determinant = 0.00 after rounding to two decimal places.
