circumference = int(input('Enter the circumeference of a tree: '))
diameter = circumference/3.14
can_be_cut_down = diameter >= 50

print(f"This tree can be cut down: {can_be_cut_down}")