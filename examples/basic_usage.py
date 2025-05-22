"""
Basic usage example of the GSO algorithm.
This example demonstrates solving a simple binary optimization problem.
"""

from gso import GSO
import numpy as np

def simple_fitness(solution):
    """Simple fitness function: maximize the number of 1s while keeping first bit 0."""
    if solution[0] == 1:  # Constraint: first bit must be 0
        return -1000
    return np.sum(solution[1:])

def main():
    print("Method 1: Using GSO.run() (Recommended)")
    # Run optimization using the static run method
    GSO.run(
        obj_func=simple_fitness, # Our fitness function
        dim=100,                  # 20-bit problem
        pop_size=50,             # Population size
        max_iter=50,            # Maximum iterations
        obj_type='max',          # Maximize the objective
        neighbour_count=3,       # Number of neighbors to interact with
        gradient_strength=0.8,   # Default gradient strength
        base_learning_rate=0.1,  # Default learning rate
        timeout=60               # 60 seconds timeout
    )
    
    print("\nMethod 2: Using GSO instance directly")
    # Create optimizer instance
    optimizer = GSO(
        pop_size=50,
        max_iter=50,
        obj_type='max',
        neighbour_count=3,
        obj_func=simple_fitness,
        gradient_strength=0.8,   # Default gradient strength
        base_learning_rate=0.1,  # Default learning rate
        dim=100
    )

    # Run optimization
    best_solution, best_fitness = optimizer.optimize()
    
if __name__ == "__main__":
    main()
    
    
    
    