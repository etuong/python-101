## _Module 5 - Files, IO, Data Encoding_

---

## Run Programs

```
python kmeans.py
```

## Approach

My approach for this assignment was to use a list of a list to manage the points. I knew the cluster had to be organized in such a way that I retrieve and update the cluster mapping. So, I decided to use a map because the keys are always going to be unique and the value can be the list of those said points.

The hardest decision was really down to set versus list. I was not too certain of how unique the points where going to be so I played it safe by choosing a list instead. To make the program generic, I knew I had to read in the first three lines. After that I didn't want to hardcode anything so I programmatically set the starting index to be 3 plus the k. In other words, point1.txt has k=4 so I knew I should start appending the points to the list at the 7th line.

To compare the size of the clusters in order to increment the convergence counter, I record the previous size in a list and then check if the integers are the same.

## Additional Information

- In the name of fun, I included Matplotlib. Please uncomment the appropriate lines to see this in action!
  - Line 4 to import matplotlib
  - Function plotClusters that plots the clusters and points
  - Lines 110 and 111 that plots the very first map
  - Line 119 that plots the very last map

## Questions

Q: This particular implementation of k-means is inefficient in terms of the number of the overall number of iterations.
Why is it inefficient and how would you fix this in your code?

A: This implementation is inefficient because we are looping through over the maximum number of iterations. The
convergence may happen much earlier than this event. We could improve this by breaking out as soon as there is no
difference in the cluster maps. But to do this, we can't just simply compare the sizes like what we are doing now
because two patients can swap clusters. We'll need to do a deep comparison.

Q: This implementation may also, depending on the input, yield incorrect answers. Specifically it may converge too
early. Why is this the case and how would you fix it?

A: The K-means algorithm requires us to randomly select points for our cluster. The input may not be randomized and this
can be a problem specifically if the points are sorted and the initial points are, say, the first four points. Also, the
points may be given such that they are nearly in their respective clusters, this could fool our program to believe that
it has already converged.
