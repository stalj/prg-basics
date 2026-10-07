import re
def f(mnumbers):
    pattern = r'^[+-]?[1-7a-dA-D]+$'
    count = 0
    for num in mnumbers:
        if re.match(pattern,num):
            count += 1
    return count
if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))
    print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))