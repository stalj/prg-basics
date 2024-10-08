###
# A program that displays your height both in cm and in feet and inches.
#
cm = float(input("Your height in cm:"))
feet = cm//30.48
inches = cm%30.48*0.3937007874016

print(f'I am {cm}cm tall, i.e. {feet} feet and  {round(inches,1)} inches')