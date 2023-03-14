# Ethan Thomas Uong, euong1

## _Module 8-9 - Object Oriented Programming_

### OCT 31, 2021

#### Python Version: 3.8.0

#### PyCharm IDE, Community Edition Version 2021.2.1

---

## Run Programs

```
python lfsr.py
python image_encrypter.py
```

## Approach

- The approach was pretty straight forward. Started out with the LFSR class and then proceeded to the encrypted image
  class. The hardest part was working with the PIL library. I did not understand why we had to open the image each time
  we were to process it. I had a hard time traversing the pixels so I relied on the width and height of the image.
  Working with int and binary was challenging and knowing how to use XOR on such types was not easy. Finally, I had to
  revisit previous lessons including the fact that tuples cannot be changed. Instead I collected the encrypted pixels
  into a list and reset the pixel tuple before saving the image.

## Known Bugs

- Not really a bug but my design is a tad off from the assignment algorithm and pseudocode. The results are consistent
  and correct, though.

## Partner Collaboration:

N/A - I worked alone on this assignment