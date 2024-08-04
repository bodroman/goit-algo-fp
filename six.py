def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням у відношені калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Ініціюємо таблицю динамічного програмування
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())

    # Заповнюємо таблицю
    for i in range(1, n + 1):
        item, data = item_list[i - 1]
        cost = data['cost']
        calories = data['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відстежуємо вибрані страви
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, data = item_list[i - 1]
            selected_items.append(item)
            w -= data['cost']

    total_calories = dp[n][budget]
    total_cost = budget - w

    return selected_items, total_calories, total_cost

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:")
print("Selected Items:", greedy_result[0])
print("Total Calories:", greedy_result[1])
print("Total Cost:", greedy_result[2])

# Динамічне програмування
dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming Result:")
print("Selected Items:", dp_result[0])
print("Total Calories:", dp_result[1])
print("Total Cost:", dp_result[2])
