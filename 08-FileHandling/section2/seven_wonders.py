seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

file_name = 'seven_wonders.txt'

seven_wonders.sort()

i = 0
with open(file_name, 'w') as sw:
    for item in seven_wonders:
        i += 1
        sw.write(f"wonder {i}: {item}\n")