import random

# Example list
items = ["apple", "banana", "cherry", "date", "elderberry"]

# Enumerate the list
fruit_list = list(enumerate(items))
for fruit in  fruit_list:
    print(fruit)
# Count number of items
count = len(items)
print(f"Total items: {count}")

# Select a random item
random_index, random_item = random.choice(fruit_list)
print(f"Random selection: {random_item} (Index: {random_index})")
"""
Exppected Results
========================= RESTART: C:/Python/random.py =========================
Total items: 5
Random selection: date (Index: 3)
========================= RESTART: C:/Python/random.py =========================
Total items: 5
Random selection: elderberry (Index: 4)

========================= RESTART: C:/Python/random.py =========================
Total items: 5
Random selection: banana (Index: 1)

"""
