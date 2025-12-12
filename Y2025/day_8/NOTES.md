<!-- cSpell:words itertools -->
## TAKEAWAY:
- DSU, Disjoint Set Union
- NamedTuple
- itertools.combinations(iterable, r)
- math.dist(p, q)

## Considerations:
- ~~"strings of lights"~~ NOPE -> there is only one line, one end and one bgn point -> middle ones drop out

## Approach #1 STUCK
1. Data class for "junction box"
    - point
    - member of circuit ?
    - is middle point

### Step 1. only once at the bgn
- for each point ~~that is not middle~~, calculate nearest distance,
- keep data of nearest distance and point

### loop: connecting boxes
- find min length for points that are not in the middle -> you should get two points
    1. both are not part of circuit:
     - update member of circuit
     - update min. length except other point
    2. one point is a part of circuit:
     - one that is already part of c. becomes middle
     - other one -> update member of c. and recalculate min. to non middles
    3. both are part of circuit
     - both becomes middle
     - merge circuit, get rid of one

## Approach #2
- Point can be NamedTuple
- need list of pairs sorted by distance

- after I got unions on DSU how to get solution: len of each tree ?