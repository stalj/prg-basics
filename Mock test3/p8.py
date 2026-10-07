def f(fnc,prods):
    ids = [fnc(p) for p in prods]
    return ",".join(ids)

if __name__ == "__main__":
    prods = ["water","cheese","tomato"]
    fnc1 = lambda x: "id:"+x[:2]
    print(f(fnc1,prods))
    fnc2 = lambda x: (x[0]+x[-1]).upper()
    print(f(fnc2,prods))