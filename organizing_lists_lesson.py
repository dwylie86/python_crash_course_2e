# Organizing a List
# Using the .sort method will permenantly sort a list, alphabetically. We can never revert to
# the original order.

# Sorting a list alphabetically is a bit more complicated when all the values are not in
# lowercase. There are several ways to interpret capital letters when determining a sort
# order, and specifying the exact order can be more complex than we want to deal with
# at this time. However, most approaches to sorting will build directly on what you
# learned in this section.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# You can also sort Z-A by putting (reverse=True) into the .sort
cars.sort(reverse=True)
print(cars)

# You can use the sorted function to temporarily sort a list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list (again):')
print(cars)

# You can use the .reverse method to print a list from back to front. It does not sort alphabetically.
cars.reverse()
print('\nList reversed:')
print(cars)

# .reverse permanently changes the list, but can be put back to normal with another .reverse
cars.reverse()
print('\nSecond reverse puts list back to normal:')
print(cars)

# The len() function will tell us how many items are in our list. Python counts the items in a list
# starting with one, so you shouldn’t run into any offby-one errors when determining the length of a list.
#  determine the amount of data
# Len is helpful if you have to manage in a visualization, or figure out the number of registered
# users on a website, among other tasks.
print(len(cars))

# Seeing the World Challenge
places_to_visit = ['bali', 'maui', 'tokyo', 'paris', 'london']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# Dinner Guests Challenge
dinner_guest_list = ['honda', 'flonda', 'moronda', 'banana', 'ruthbrut', 'santa']
number_invited = len(dinner_guest_list)
print(f'I am inviting {number_invited} people to dinner')

# Avoiding Index Errors When Working With Lists
# Traceback errors occur when you attempt to access an index not in a list,
# i.e. position 4 in a list of 3 items. Use -1 to go from the right to access the last item in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

# You'll only get an error if the list is empty when using the negative approach.
# If an index error occurs and you can’t figure out how to resolve it, try printing your 
# list or just printing the length of your list. Your list might look much different than 
# you thought it did, especially if it has been managed dynamically by your program. 
# Seeing the actual list, or the exact number of items in your list, can help you sort out 
# such logical errors.
