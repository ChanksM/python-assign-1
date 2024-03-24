# task 1
original_list = list(range(1, 21))

# task 1.1
new_list = original_list[4:15]

# task 1.2
print("Elements of the original list:")
for num in original_list:
    print(num)

print("\nElements of the new list")
for num in new_list:
    print(num)


# Task 2
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population


# Task 2.1
cities = [
    City("Tbilisi", 3_623_000),
    City("Rustavi", 898_000),
    City("Kutaisi", 705_000),
    City("Batumi", 320_000),
    City("Mestia", 30_000)
]

# Task 2.2
total_population = sum(city.population for city in cities)

print("Total population of the cities:", total_population)
