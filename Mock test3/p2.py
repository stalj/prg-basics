class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x > 0 and self.y > 0: return 1
        if self.x < 0 and self.y > 0: return 2
        if self.x < 0 and self.y < 0: return 3
        if self.x > 0 and self.y < 0: return 4
        return 0
    
    def m2(self,a,b):
        point_another = C(a,b)
        return self.m1() == point_another.m1()
    
    def m3(self,a,b):
        distance = ((self.x - a)**2 + (self.y - b)**2)**0.5
        return distance > 5

if __name__ == "__main__":
    p = C(2,3)
    print(p.m1())
    print(p.m2(7,4))
    print(p.m2(-3,1))
    print(p.m3(8,5))
    print(p.m3(4,7))
