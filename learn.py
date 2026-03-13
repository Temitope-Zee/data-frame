# deforestation_rate = [150, 145, 140, 135, 130]
# deforestation_year = [2010, 2011, 2012, 2013, 2014]

# for rate in deforestation_rate:
#     print(f"rate = {rate}")

#     for year in deforestation_year:
#         print(f"deforestation year = {year}")

#         for i in range(len(deforestation_rate)):
#             rate = deforestation_rate[i]
#             year = deforestation_year[i]
#             print(f"i = {i} - yearly deforestation rate in {year} is: {rate} k hectares")

# for i,  rate in enumerate(deforestation_rate):
#     year = deforestation_year[i]
#     print(f"i = {i} - yearly deforestation rate in {year} is: {rate} k hectares")

#     marine_specie_count ={'dolphin':12,
#                           'whale':3,
#                           'sea_turtles':7
#                           }
    
#     for specie in marine_specie_count:
#         print(f" {specie}: {marine_specie_count[specie]} sightings")

#         marine_species_count = {
#     'Dolphins': 12,
#     'Whales': 3,
#     'Sea Turtles': 7
# }

# for species, count in marine_species_count.items():
#     print(f"{species}: {count} sightings")

#     deforestation_data = {
#         'Amazon': 120,
#         'Congo Basin': 80,
#         'Southeast Asia': 95,
#         'Eastern Australia': 40
#     }
#     critical_threshold = 90
#     for region, area in deforestation_data.items():
#         if area > critical_threshold:
#             print(f"Critical deforestation in {region}: {area} square kilometres")

            
            
#             ocean_temperature = {
#                 'Pacific': [25, 25.3, 25.6, 25.2, 25.5, 25.6],
#                 'Atlantic': [23.4, 23.8, 23.7, 29.9, 24.0, 29.1],
#                 'Indian': [26.5, 26.7, 27.0, -29, -55, -99, -99]
#             }
# for ocean, temperature in ocean_temperature.items():

#     print(f"ocean: {ocean}: sum of all the temperatures in this list : {sum(temperature)}")
   
            
def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


def recursive_linear_search(arr, target, index=0):
    # Base Case: Target not found (reached the end)
    if index >= len(arr):
        return -1
    
    # Base Case: Target found
    if arr[index] == target:
        return index
    
    # Recursive Step: Move to the next index
    return recursive_linear_search(arr, target, index + 1)

# Example:
my_list = [5, 2, 9, 1, 7]
print(recursive_linear_search(my_list, 1)) # Output: 3

content = """
s = 'Hello ' 

def say_hi(name):
    print(s + name)

class Greet:
    pass
"""

# Contents of the module we are creating 
content = """
s = 'Hello ' 

def say_hi(name):
    print(s + name)

class Greet:
    pass
"""

# Write the above text to a file called my_module.py
# within our current working directory. 
with open('./my_module.py', 'w') as fp:
    fp.write(content)

    #Import the module we've just made! 
import my_module

try:
    # Try to print the variable s
    print(s)
except NameError:
    # We've caught a NameError exception (error!)
    # We inform the programmer (you) that the variable does not exist
    print("Variable 's' does not exist!")

    my_module.s

    # Accessing the say_hi function in my_module
my_module.say_hi('Zainab')

# Alias for my_module
import my_module as md

# Accessing the variable s using an alias
md.s

# Accessing the say_hi function using an alias for my_module
md.say_hi('Temitope')

# Accessing the empty class, Greet
md.Greet

from my_module import *

help('modules')

ratings = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [3, 6, 9, 12, 15]]) # type: ignore
ratings.shape = (5, 3)
print(ratings)