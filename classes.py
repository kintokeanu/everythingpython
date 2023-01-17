class Robot:

    def __init__(self, name, color, weight,):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


class Person:
    
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.isSitting = i

    def sit_Down(self):
        print("my name is " + self.name)



r1 = Robot("brian", "black", "57")
r2 = Robot("Finn", "golden brown", "10")

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "aggressive", True)

p1.robot_owned = r2
p2.robot_owned = r1


p1.robot_owned.introduce_self()

