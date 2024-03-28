
# Table of Contents

1.  [heap sort](#org37e4d71)


<a id="org37e4d71"></a>

# heap sort

When I was reading a textbook on algorithms around 2017 or so I
decided to implement a heap sort in python to see how it turned out. I
wrote a verification routine and it turned out the algorithm was
producing errors. <&nil>

Afterwards I decided to find out which other algorithms worked.

I checked many of the usual places online

-   stack overflow <&nil>
-   geeks for geeks <&nil>
-   Wikipedia Heap Sort <&nil>
-   MIT Introduction to Algorithms <&nil>

I wrote two programs, a number generator, and a heap sort
implemented in three variations.

-   heapsort (3 implementations) [heapsort.py](heapsort.py)
-   number-generator [number-generator.py](number-generator.py)

I found that nearly all the sources were wrong. They had subtle bugs
in them that only appeared in larger sets.

I determined that Wikipedia and MIT Introduction to Algorithms had the
correct implementation was a top-down solution. The "bubble-up" bottom
up solution from Essential Algorithms <&nil> was wrong.

I wrote my own variation and tested all of them. The source includes
the capability to generate graphiz tree diagrams of the heap as well.

This exercise clearly demonstrates the importance of testing, but also
testing at scale to reveal bugs that don't appear in trivial tests.

