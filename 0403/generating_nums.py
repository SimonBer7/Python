import numpy as np

# Define the set of grades
grades = [1, 2, 3, 4, 5]

# Probabilities of selection
probabilities = [0.10, 0.25, 0.25, 0.28, 0.12]

# Generating 15 grades with the given probabilities
generated_grades = np.random.choice(grades, 15, p=probabilities)

# Printing the generated grades
print("Generated grades:", generated_grades)
