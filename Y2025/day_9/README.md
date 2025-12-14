# Day 9

## Part 1
Easy

## Part 2
The question is does given rectangle overlap the green shape template, mind that green one shape is not siple rectangle

Potential Optimizations:
- sort rectangles by area, check bigger ones first, if overlap found early can skip smaller ones

### Brute Force
- Calculate all points that form green template shape,
    - WOW how to find out which part is inside vs. outside green tiles (???)
    - ^^^ one way would be using grid, first connect points than line by line fill gaps between, mind that there can be several gaps between
    - GOTCHA: big problem with algo for filling gaps is that shape can be concave, so simple left-right fill will not work
- for each combination pair check if overlap green template

### concept
- try implement grid class
- hard part is to fill the green shape

### The Problem and Solution
The Problem
Your grid initialization iterates over ~9.3 billion cells! That's the bottleneck.

Issue and Complexity
- Fill loop ->	O(width × height) = ~9.3 billion iterations
- Each iteration creates Point objects -> Additional memory overhead

Solutions:
1. Don't materialize the grid
For this problem, you likely don't need to store every green point. Consider using:

- Shoelace formula for polygon area
- Pick's theorem (???)

2. Use coordinate compression
Map the ~495 unique x/y values to indices 0-494, reducing the grid to ~495×495 = 245,025 cells.

3. Work with line segments
Instead of filling the grid, keep track of horizontal/vertical line segments and check overlaps mathematically.

### Grid Compression Approach FAILED ATTEMPT
1. Map points to compressed coordinates (all points are unique)