# Changing, Adding, and Removing Elements
# The syntax for modifying an element is similar to the syntax for accessing
# an element in a list. To change an element, use the name of the list followed
# by the index of the element you want to change, and then provide the new
# value you want that item to have.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Use .append method to add an item at the end of a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# You can use .append to dynamically build a list.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Use .insert method to insert an item at an index in a list.
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Use the del statement to delete items at an index of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Use the .pop method to remove the last item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# The pop method is also useful for grabbing the most recent item if the list is store chronologically
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# You can also pop items from any index in a list.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# IMPORTANT NOTE! Whenever you pop an item from a list, it is no longer stored in the list!
print(motorcycles)

# You can also use the .remove method to remove specific values from a list. Either as a string...
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#...or a variable string.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# NOTE: .remove method will only remove the first occurrence of a value in a list. If a list has repeated
# values, you'll have to use a loop to remove all occurrences of it.

# Guest List Challenge
guest_list = ['honda', 'flonda', 'moronda', 'banana']
guest_1_message = f"I would like to invite {guest_list[0].title()} to dinner."
guest_2_message = f"I would like to invite {guest_list[1].title()} to dinner."
guest_3_message = f"I would like to invite {guest_list[2].title()} to dinner."
guest_4_message = f"I would like to invite {guest_list[3].title()} to dinner."
print(guest_1_message)
print(guest_2_message)
print(guest_3_message)
print(guest_4_message)

# Changing Guest List Challenge
print(guest_list)
# Banana can't make it, Ruthbrut will take their place.
guest_list[3] = 'ruthbrut'
guest_1_message = f"I would like to invite {guest_list[0].title()} to dinner."
guest_2_message = f"I would like to invite {guest_list[1].title()} to dinner."
guest_3_message = f"I would like to invite {guest_list[2].title()} to dinner."
guest_4_message = f"I would like to invite {guest_list[3].title()} to dinner."
print(guest_list)

# More Guests Challenge
# Adding guest at beginning
guest_list.insert(0, 'thronda')
# Adding guest at middle
guest_list.insert(3, 'cletus')
# Adding guest at end
guest_list.append('santa klusk')
print(guest_list)

# Shrinking Guest List Challenge
print('\nYou can now only invite two people to dinner, Ruthbrut and Santa Klusk\n')

# Once I learn loops, I can automate this, but for now I'm popping and deleting.
not_invited_1 = guest_list.pop(0)
print(f"You are the weakest invite, {not_invited_1.title()}, goodbye.")
not_invited_2 = guest_list.pop(0)
print(f"You are the weakest invite, {not_invited_2.title()}, goodbye.")
not_invited_3 = guest_list.pop(0)
print(f"You are the weakest invite, {not_invited_3.title()}, goodbye.")
not_invited_4 = guest_list.pop(0)
print(f"You are the weakest invite, {not_invited_4.title()}, goodbye.")
not_invited_5 = guest_list.pop(0)
print(f"You are the weakest invite, {not_invited_5.title()}, goodbye.")

print(f"\nGreat news {guest_list[0].title()} and {guest_list[1].title()}! You're still invited.\n")

# Clearing out the list, could loop this too.
del guest_list[0]
del guest_list[0]

# Printing empty list
print(guest_list)
