class SmartHome:
    def __init__(self,name):
        self.name = name

    def on(self):
        pass
    
    def off(self):
        return f"{self.name} is off"

class Fan(SmartHome):
    def on(self):
        return f"{self.name} fan is on. Its going to blow fresh air! "

class Light(SmartHome):
    def on(self):
        return f"{self.name} light is on. It has bright light "

class AC(SmartHome):
    def on(self):
        return f"{self.name} AC is on. Its going to throw fresh and cool air! "
    
equipments = [
    Fan("Atomberg"),
    Light("Orient Electric"), 
    AC("Voltas")
    ]

for i in equipments:
    print(i.on())
