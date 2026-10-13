class C:
    def __init__(self,value):
        self.counter = value

    def m1(self):
        return self.counter
    def m2(self):
        self.counter += 1
    def m3(self):
        self.counter -= 1
    def m4(self,n):
        self.counter += n

    def __str__(self):
        return str(self.counter)

if __name__ == "__main__":
    c=C(5)
    print(c.m1())
    print(c.m2())
    print(c.m1())
    print(c.m4(-8))
    print(c.m1())
    print(c.m3())
    print(c.m1())
    print(c.m4(10))
    print(c.m1())
    print(c.__str__())