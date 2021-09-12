# AI_7th_Sem

## Puzzle  

Given a 3×3 board with 8 tiles (every tile has one number from 1 to 8) and one empty space.
The objective is to place the numbers on tiles to match the final configuration using the empty space.
We can slide four adjacent (left, right, above, and below) tiles into the empty space.
<p align="center">
    <img src = "/Users/sahajsingh/Desktop/AI_7th_Sem/Images/play1.png" width=300>
    <br>A screenshot of the gameplay
</p>
Algorithm :
   c(x) = f(x) + h(x) where
   f(x) is the length of the path from root to x
        (the number of moves so far) and
   h(x) is the number of non-blank tiles not in
        their goal position (the number of mis-
        -placed tiles). There are at least h(x)
        moves to transform state x to a goal state

* Algorithm LCSearch uses c(x) to find an answer node
* LCSearch uses Least() and Add() to maintain the list
     of live nodes
* Least() finds a live node with least c(x), deletes
     it from the list and returns it
* Add(x) adds x to the list of live nodes
* Implement list of live nodes as a min-heap
