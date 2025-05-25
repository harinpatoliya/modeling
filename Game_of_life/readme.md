📘 CODE DESCRIPTION: Conway’s Game of Life from an Image
Author: Harin Patoliya

This Python script models Conway's Game of Life using an input image as the
initial configuration. The Game of Life is a cellular automaton where each cell
can be either alive or dead, and its state evolves over discrete time steps
according to simple rules based on the states of neighboring cells.

This script turns the pixels of a color image into a grid of cells (black = dead,
white = alive), then simulates and visualizes their evolution over time.

🧠 CONWAY'S GAME OF LIFE – RULES

Conway's Game of Life is a cellular automaton devised by mathematician 
John Horton Conway. It consists of a 2D grid of cells that evolve over time
based on a few simple rules.

Each cell in the grid has two possible states:
- ALIVE (1 or white)
- DEAD  (0 or black)

Each cell interacts with its 8 neighboring cells:
(top, bottom, left, right, and 4 diagonals)

At each time step (generation), the following rules determine the next state
of every cell in the grid:

RULE 1: UNDERPOPULATION
If a cell is ALIVE and has FEWER than 2 live neighbors → it DIES.
(Too few neighbors – loneliness)

RULE 2: SURVIVAL
If a cell is ALIVE and has 2 or 3 live neighbors → it STAYS ALIVE.
(The cell has just the right number of neighbors)

RULE 3: OVERPOPULATION
If a cell is ALIVE and has MORE than 3 live neighbors → it DIES.
(Too many neighbors – overcrowding)

RULE 4: REPRODUCTION
If a cell is DEAD and has EXACTLY 3 live neighbors → it becomes ALIVE.
(Perfect condition for a new cell to be born)

SUMMARY TABLE:

| Current State | Number of Live Neighbors | Next State | Rule Applied       |
|---------------|--------------------------|------------|--------------------|
| Alive         | < 2                      | Dead       | Underpopulation    |
| Alive         | 2 or 3                   | Alive      | Survival           |
| Alive         | > 3                      | Dead       | Overpopulation     |
| Dead          | Exactly 3                | Alive      | Reproduction       |
| Dead          | Not 3                    | Dead       | Remains Dead       |

NOTES:

- All updates happen simultaneously for all cells in each generation.
- The grid can show static shapes, oscillating patterns, or moving structures.
- Despite its simplicity, the Game of Life can simulate complex systems.

 RUN THE SIMULATION
 
- User can use default image file for the simulation or can use his&her's own image.
- Name of image should be finimage.png.
- Model generate 100 generations based on rules from intial phase.

