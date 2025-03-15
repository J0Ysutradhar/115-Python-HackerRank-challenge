# HackerRank Problem: Finding the Percentage1

## Problem Statement

You have a record of **N** students. Each record contains the student's name and their grades in the following three subjects: Mathematics, Physics, and Chemistry. The marks can be floating-point numbers. Your task is to find the average marks obtained by a particular student, rounded to **2 decimal places**.

### Input Format
- The first line contains an integer, **N**, the number of students.
- The next **N** lines contain the name of a student and their grades in Mathematics, Physics, and Chemistry, separated by space.
- The final line contains the name of a student for whom you want to calculate the average grade.

### Constraints
- **2 \<= N \<= 10**
- **0 \<= Marks \<= 100**

### Output Format
Print the average of the marks obtained by the specified student, rounded to **2 decimal places**.

### Sample Input 0
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

### Sample Output 0
```
56.00
```

### Explanation 0
- Marks for Malika are **52**, **56**, and **60**. Their average is:
  
  ```
  (52 + 56 + 60) / 3 = 56.00
  ```

### Sample Input 1
```
2
Harsh 25 26.5 28
Anurag 100 100 100
Harsh
```

### Sample Output 1
```
26.50
```

### Explanation 1
- Marks for Harsh are **25**, **26.5**, and **28**. Their average is:
  
  ```
  (25 + 26.5 + 28) / 3 = 26.50
  
