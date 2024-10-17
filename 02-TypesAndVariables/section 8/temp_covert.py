temp = int(input('Enter the temperature in Celsius: '))
kelvin = temp + 273.15
fahrenheit = temp * (9/5) + 32

print(f"temp in C: {temp}")
print(f"temp in K: {kelvin:.1f}")
print(f"temp in F: {fahrenheit}")