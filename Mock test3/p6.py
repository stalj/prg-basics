class C:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        initials = self.first_name[0] +self.last_name[0]
        if self.age >= 18:
            res = initials.upper()
        else:
            res = initials.lower()
        return f"{res}{self.age}"

if __name__ == "__main__":
    print(C("John","May",21))
    print(C("Anna","Brown",17))