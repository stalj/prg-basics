def f(fnc,res):
    filtered = [x for x in res if fnc(x)]
    if not filtered:
        return 0
    return max(filtered) - min(filtered)

if __name__ == "__main__":
    res = [95,90,20,50,70]
    fnc1 = lambda x: x>50
    print(f(fnc1,res))
    fnc2 = lambda x: x>30 and x<90
    print(f(fnc2,res))