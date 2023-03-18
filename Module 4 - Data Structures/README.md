## _Module 4 - Data Structures_

---

## Run Programs

```
python nbody.py
```

## Exercise

The physics formulas and equations were given as well as the input file which contains the four planets and sun with their properties like x and y positions and velocities and mass.

The approach was to first calculate the distance between the two objects, which in this case is always the planet itself and the sun, and then calculate the gravitational force between them. The resultant force, and therefore acceleration and velocities, gets vectorized into their respective x and y parts to be concatenated with the planet's current properties.

The above computation iterates until the total time overlaps or exceeds the input time. The total time gets updated after each iteration with the time step. The final thing to do is to print the output (planet's final properties) using scientific notation.
