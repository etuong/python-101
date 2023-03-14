# Ethan Thomas Uong, euong1

## _Module 6 - Functions_

### OCT 10, 2021

#### Python Version: 3.8.0

#### PyCharm IDE, Community Edition Version 2021.2.1

---

## Run Programs

```
python catalan.py
python pascal.py
```

## Approach

For catalan.py my approach was to use recursion. The same problem can be done using primitive loop or dynamic
programming. To use recursion, I needed a base condition which in this case is when k is less than n. If so, it recurses
the same function and multiply its output. I picked this approach because it seems to be the most straightforward to me.

For pascal.py my approach was sort of like top down, meaning I worked backward by starting with the last row of the
triangle. The recursion takes the row entries from the previous level to calculate the current entry based on their
positions. It seems to work fine. Initially I wanted to print the row as I go but that proved to be difficult. So, I
tackled this problem by storing the rows using a list inside a list and printing the whole triangle at the very end.

## Known Bugs

- In catalan.py, since we are dividing (n+k)/k the result will be a float, but since the output expects an integer, I
  convert the float to an int at the very end when I display the catalan numbers. As a result, there is some rounding
  differences. The only known difference is when the order is 14. Solution output has it as 9694845 whereas mine reads 9694844. 
