###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# reading of temperature in Celsius
temperatureC = float(input("Temperature in Celsius: "))
# converting for temperature in Kelvins and Farenheith
temperatureK = temperatureC+273.15
temperatureF = temperatureC*1.8+32
# showing results
print(f"Temperature in Kelvins: {temperatureK}")
print(f"Temperature in Farenheith: {round(temperatureF, 2)}")