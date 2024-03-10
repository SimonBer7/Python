import numpy as np

# Definice parametrů normálního rozdělení
mean_salary = 38355  # Průměrná mzda
std_dev_salary = 14225  # Směrodatná odchylka

# Generování dat o průměrné mzdě zdravotních sester
salary_data = np.random.normal(mean_salary, std_dev_salary, 1000)
print("Salary data for 1000 nurses:")
print(salary_data)

# Definice parametrů binomického rozdělení
n_trials = 5  # Počet pokusů (hodů kostkou)
probability_success = 0.16  # Pravděpodobnost úspěchu (padne šestka)

# Generování dat v binomickém rozdělení
dice_rolls = np.random.binomial(n_trials, probability_success, 100)
print("Dice rolls for 100 trials with binomial distribution:")
print(dice_rolls)
