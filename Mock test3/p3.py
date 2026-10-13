def f(d):
    if not d:
        return 0
    passengers = d.values()
    average = sum(passengers)/len(passengers)
    count = 0
    for num in passengers:
        if num > average:
            count += 1
    return count

if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))