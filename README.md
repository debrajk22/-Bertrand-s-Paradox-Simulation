# Bertrand's Paradox Simulation
This repository contains bertrands_paradox.ipynb Jupyter notebook that samples random objects to explore Bertrand's Paradox.
The simulation takes into account *1 million* random cases to calculate the required probabilities.
We consider a unit circle (circle of radius 1) and an inscribed equilateral triangle of side length sqrt(3) for simulating the probabilities.

**The notebook simulates 4 functions -**
1. **bertrands_paradox_actual function:** simulates the actual problem statement of the paradox that is length of the chord being greater than the side of the equilateral triangle. This simulation gives a probability of around **0.333526** for the chord being greater than the side of inscribed triangle.
2. **bertrands_paradox_distance_of_midpt_from_centre function:** simulates the distance of the midpoint of the chord being and compares it with 1/2. This simulation gives a probability of around **0.204134** for the chord being greater than the side of inscribed triangle.
3. **bertrands_paradox_fixing_one_point function:** simulates chords by fixing one point and varying the other on the circumference of the circle. This simulation gives a probability of around **0.333504** for the chord being greater than the side of inscribed triangle.
4. **bertrands_paradox_taking_parallel_lines function:** simulates by taking parallel lines and checking the probability of the chord being longer than the side of the equilateral triangle. This simulation gives a probability of around **0.499714** for the chord being greater than the side of inscribed triangle.
