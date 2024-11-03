import cm_to_inch
import feet_inch_to_cm
import cm_to_feet

feet = float(cm_to_feet.convert4(15))

print("Inches: ", cm_to_inch.convert1(15))
print("Centimetres: ", feet_inch_to_cm.convert2(15))
print("Centimetres: ", feet_inch_to_cm.convert3(15))
print(f"Feet:  {feet:.2f}")