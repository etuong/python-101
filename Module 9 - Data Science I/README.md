## _Module 11 - Data Science_

---

## Run Programs

```
python hill.py
```

## Approach

My approach for this assignment was to not reinvent the wheel. I wanted to reuse as many features from Numpy as I can.
This included finding the determinant and checking to see if the matrix is a square matrix.

For the mod_inverse function, I wanted to keep it simple so I used the naive approach which was literally to loop
through a range and checking if the modulus of 26 to that number yields one.

The encrypt and decrypt functions are similar on purpose because the printing of the text and matrices is modular. My
approach was to spend more time on the encrypt function because I knew the decrypt function was going to be very
similar.

The hardest part of the assignment was learning how to access and modify the elements of the numpy array. So to keep it
simple, I just update the elements in-place. Lastly, I learned that numpy integer data are actually numpy.int32 or
numpy.int64 which are not the same as the Python primitives.
