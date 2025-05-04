import random
from enum import Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
  
# Iterating over Enum members
print("\nThe following are the days of the week:")
for day in  Weekday:
    print(day.name, day.value)

print("\nDays of the week in reverse:")
for day in reversed(Weekday):
    print(day.name)

count = len(Weekday)
print(f"\nThere are {count}","days in a week")

# Enumerate the list
enumerated_items = list(enumerate(Weekday))
# Select a random item
random_index, random_item = random.choice(enumerated_items)
#print(f"Random selection: {random_item} (Index: {random_index})")
print(f"\n{random_item}","is one of those days")
"""
random_index, random_item = random.choice(enumerate(Weekday))
TypeError: object of type 'enumerate' has no len()
#print(f"Random selection: {random_item} (Index: {random_index})")
print(f"\n{random_item}","is one of them")
"""
# Define and print weekend days on the same line
WEEKEND = {Weekday.SATURDAY, Weekday.SUNDAY}
print("\nThe weekend is ", ", ".join(day.name for day in WEEKEND))

Chores = (Weekday.MONDAY,Weekday.WEDNESDAY, Weekday.FRIDAY)
print("\nOne of my week day chores is to\nfeed the cat on", ", ".join(day.name for day in Chores))
 
print("\nA daily chore is to\ndo the dishes on", ", ".join(day.name for day in  Weekday))
"""
EXPECTED OUTPUT


The following are the days of the week:
MONDAY 1
TUESDAY 2
WEDNESDAY 3
THURSDAY 4
FRIDAY 5
SATURDAY 6
SUNDAY 7

Days of the week in reverse:
SUNDAY
SATURDAY
FRIDAY
THURSDAY
WEDNESDAY
TUESDAY
MONDAY

There are 7 days in a week

Weekday.FRIDAY is one of those days

The weekend is  SUNDAY, SATURDAY

One of my week day chores is to
feed the cat on MONDAY, WEDNESDAY, FRIDAY

A daily chore is to
do the dishes on MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY

"""
