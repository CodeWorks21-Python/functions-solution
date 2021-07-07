# --------------- Section 3 --------------- #
# 1 | Fahrenheit to Celsius Conversion
#
# Fahrenheit is way we measure temperature and is commonly used in the United States, the Cayman Islands, and Liberia.
# The other unit of measurement is celsius. Celsius is commonly used throughout the rest of the world. Since they are
# different units of measurement, then the exact same temperature will have different values.
#
# For example, 68° fahrenheit is 20° celsius.
# https://www.google.com/search?client=firefox-b-1-d&q=68+degrees+fahrenheit+to+celsius
#
#
# To calculate celsius from fahrenheit, you use the following equation:
#   c = (f - 32) * (5/9)
#       where; f represents degrees fahrenheit
#              c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in fahrenheit to celsius.
#   2 - Define a function that will convert a temperature in celsius to fahrenheit.
#   3 - Return the new temperature.
#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   72° fahrenheit is 22.2222° celsius
#   10° celsius is 50° fahrenheit
#
# WRITE CODE BELOW
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


og_temperature = 65  # this will be used as the original temperature in fahrenheit and celsisus

temperature = fahrenheit_to_celsius(og_temperature)
print(str(og_temperature) + '° Fahrenheit is ' + str(temperature) + '° Celsius')

temperature = celsius_to_fahrenheit(og_temperature)
print(str(og_temperature) + '° Celsius is ' + str(temperature) + '° Fahrenheit')
print()


# 2 | Celsius to Kelvin
#
# There is another unit of measurement, called kelvin. It is closely related to celsius. In fact to convert an equation
# from Celsius to Kelvin is as thus:
#   k = c + 273.15
#   where; c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in celsius to kelvin.
#   2 - Define a function that will convert a temperature in kelvin to celsius.
#   3 - Return the new temperature.
#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   45° celsius is 318.15° kelvin
#   232° kelvin is -41.15° celsius
#
# WRITE CODE BELOW
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


og_temperature = 52  # this will be used as the original temperature in fahrenheit and celsisus

temperature = celsius_to_kelvin(og_temperature)
print(str(og_temperature) + '° Celsius is ' + str(temperature) + '° Kelvin')

temperature = kelvin_to_celsius(og_temperature)
print(str(og_temperature) + '° Kelvin is ' + str(temperature) + '° Celsius')
print()


# Question: How could you use these functions to convert a temperature in fahrenheit to kelvin?

# You can convert from fahrenheit to celsius, and then celsius to kelvin.

og_temperature = 82  # this is in fahrenheit

temperature = fahrenheit_to_celsius(og_temperature)    # convert fahrenheit to celsius
temperature = celsius_to_kelvin(temperature)        # then convert celsius to kelvin

print(str(og_temperature) + '° Fahrenheit is ' + str(temperature) + '° Kelvin')