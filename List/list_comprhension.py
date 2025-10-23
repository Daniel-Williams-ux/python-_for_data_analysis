# Scenario: You have a dataset of temperatures in Celsius and you want only the temperatures above 25°C.
# syntax: [expression for item in iterable if condition]
# Why it matters in analysis: 
# This is like subsetting data — essential for feature selection or analysis of specific conditions.
temperatures = [22, 27, 19, 30, 25, 28, 21]

hot_tempreatures = [temp for temp in temperatures if temp > 25]
#print(hot_tempreatures)  # Output: [27, 30, 28]

# equivalent using loop
temperatures = [22, 27, 19, 30, 25, 28, 21]
hot_temperatures = []
for t in temperatures:
    if t > 25:
        hot_temperatures.append(t)
print(hot_temperatures)  # Output: [27, 30, 28]


# simple transformation
a = [1, 2, 3]
doubles = [x * 2 for x in a]            # [2, 4, 6]

# function call / tuple construction
strings = [str(x) for x in a]           # ['1','2','3']
pairs = [(x, x**2) for x in a]          # [(1,1),(2,4),(3,9)]

# filter vs ternary inside expression
filtered = [x for x in a if x > 1]                      # [2,3]
mapped_with_ternary = [x if x > 1 else 0 for x in a]     # [0,2,3]
