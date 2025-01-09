# List Comprehensions

**Task**

You are given three integers **x**, **y**, and **z** representing the dimensions of a cuboid along with an integer **n**. Print a list of all possible coordinates on a 3D grid where the sum of the coordinates is not equal to **n**. Here, **0 <= i <= x**, **0 <= j <= y**, **0 <= k <= z**.

Use list comprehensions to generate the desired list.

**Input Format**

Four integers **x**, **y**, **z**, and **n** are given on separate lines, respectively.

**Constraints**

- \( 0 \leq x, y, z \leq 100 \)
- \( 0 \leq n \leq x + y + z \)

**Output Format**

Print the list in lexicographic increasing order.

**Sample Input 0**
```
1
1
1
2
```

**Sample Output 0**
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

**Explanation**

Given \( x = 1, y = 1, z = 1, n = 2 \):
- Possible coordinates are \([0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]\).
- Removing coordinates where the sum is equal to 2, we are left with \([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\).

