# Genetic Learning
## Features
#### Space-bar (Hold)
- Freeze's objects in their place and shows all objects if they are hidden
#### "R" Key (Toggle)
- Hides all objects except for the best path from the past generation
## Hyper-Parameters

- Number of balls
  - The number of balls will allow you to reach the target faster by raising your odds of having a potitive mutation
  - This will cause the program to stutter depending on your computing power 
- Starting Moves
  - This hyperparameter determines the number of moves that the AI can make in order to reach the target
  - If the number of starting moves is small, the number of mutations must be higher to prevent mutations from creating
  objects with the same movements
- Min-Max Velocity
  - This is the range of moves that the AI can make in its pursuit of the target
- Generation Saved
  - This is the percentage of the current generation that is preserved onto the next generation
  - The inverse of this number multiplied by the total is the number of children that are created
- Best Parent Saved
  - This is the percentage of children that will be mutated from the best ball in the past generation
  - The larger this number, the less random the children will be due to the lack of combination of genes from other 
  top parents
- Mutation Rate
  - The mutation rate is the rate/percentage of individual vectors changed per child
  - The higher this rate, the more the randomness
- Starting X and Y
  - The starting position of the points each generation
- Target
  - The target for the AI to reach

## Learning Methods
### Child Creation 
The creation of a child is the most important part of the Genetic Learning Model.
The three steps of child creation are parent selection, chromosome crossover, and mutation.
#### Parent Selection
For the selection of parents, the top **{generation_saved}**% of all objects will be passed on
to the next generation as well as being put into the gene pool for the children of the next generation.
**{best_parent_saved}**% of the kids will have the moves of the best object in the net.
#### Crossover
Genetic crossover is used to mix an attribute from each parent to create a child. In this case, the child will have the 
first half of its move from its first parent, and its second half of its move from its second parent. This will allow 
the child to test the best parts of the best objects in the net to form the best child as possible.
#### Mutation
The mutation of the child vectors is important for the net to be able to learn the best moves. These mutations will have
a chance to push the children closer to the target than the parent, and therefore become a parent in the next 
generation. Allowing some children to be a direct descendant of the best parent allows for their mutated children
to have higher chances to beat their parent to become the best node than their other child counterparts.
## Fitness Function
The fitness function is made up of the distance of the object of the target (in pixels), plus the number of moves that 
it has taken the object to get to the target. For this function, it was chosen to raise the distance to the power of 5 
to prioritize getting closer to the target, before limiting moves. The result of the fitness function is stored in a 
hashmap with the object for future use.