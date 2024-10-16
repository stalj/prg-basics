# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')

if __name__ == "__main__":
    main()