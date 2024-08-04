import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Задаємо кількість симуляцій
NUM_SIMULATIONS = 100000

# Симулюємо кидки двох кубиків
dice1 = np.random.randint(1, 7, NUM_SIMULATIONS)
dice2 = np.random.randint(1, 7, NUM_SIMULATIONS)
sums = dice1 + dice2

# Підраховуємо кількість кожної можливої суми
sum_counts = np.zeros(13)
for sum_value in sums:
    sum_counts[sum_value] += 1

# Обчислюємо ймовірності
sum_probabilities = sum_counts / NUM_SIMULATIONS

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Порівнюємо результати
sums_range = range(2, 13)
simulation_probs = [sum_probabilities[i] for i in sums_range]
analytical_probs = [analytical_probabilities[i] for i in sums_range]

# Показуємо результати
plt.figure(figsize=(10, 6))
plt.bar(sums_range, simulation_probs, alpha=0.5, label='Симуляція')
plt.plot(sums_range, analytical_probs, 'r--', marker='o', label='Аналітичні')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.savefig('probabilities_plot.png')
plt.show()

# Будуємо таблицю ймовірностей
table_data = {
    'Сума': sums_range,
    'Ймовірність (симуляційна)': simulation_probs,
    'Ймовірність (аналітична)': analytical_probs
}

df = pd.DataFrame(table_data)
print(df)
df.to_csv('probabilities_table.csv', index=False)
