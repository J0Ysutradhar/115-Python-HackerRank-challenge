# Write a Function

**Task**

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
1. The year can be evenly divided by 4, is a leap year, unless:
   2. The year can be evenly divided by 100, it is NOT a leap year, unless:
      3. The year is also evenly divisible by 400. Then it is a leap year.

This means that 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years.

Write a function that takes an integer representing a year as input and returns a boolean value indicating whether it is a leap year.

**Input Format**

Read **year**, the year to check.

**Constraints**

- \( 1900 \leq \text{year} \leq 10^5 \)

**Output Format**

Your function must return a boolean value (True/False). The output is handled by the provided code template.

**Sample Input 0**
```
1990
```

**Sample Output 0**
```
False
```

**Explanation**

1990 is not divisible by 4, so it is not a leap year.




