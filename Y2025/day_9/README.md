# Day 9

## Part 1
Easy

## Part 2
The question is does given rectangle overlap the green shape template, mind that green one shape is not siple rectangle

### Brute Force
- Calculate all points that form green template shape,
    - WOW how to find out which part is inside vs. outside green tiles (???)
    - ^^^ one way would be using grid, first connect points than line by line fill gaps between, mind that there can be several gaps between
- for each combination pair check if overlap green template

### concept
- try implement grid class