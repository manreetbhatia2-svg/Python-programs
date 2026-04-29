# classes
# Encapsulation
class introduction:
    def __init__ (self,gender,location):
        self.gender = gender
        self.location = location
        
    def intro(self,name,age):
        self.name = name
        self.age = age
        return (f"My name is {name} and I am {age} years old. I am from {self.location}.")
    
    def education(self,school,grade,division):
        self.school = school
        self.grade = grade
        self.division = division
        return(f"I study in {school} and I am in grade {grade}{division}")
        
    def hobbies(self,play,read):
        self.play = play
        self.read = read
        return(f"My hobbies include playing {play} and I like reading {read} books")
      
# Inheritance and polymorphism
class student(introduction):
    def intro (self,name,age):
        return(f"I am a student. My name is {name} and I am {age} years old. I live in {self.location}")
    
class prof(introduction):
    def intro(self,name,age):
        return(f"I am a professor. My name is {name} and I am {age} years old. I live in {self.location}")
    
girl = introduction("Female","Pune")
print(girl.intro("Manya",30))
print(girl.education("DPS",11,"A"))
print(girl.hobbies("Badminton","thriller"))
print("\n")  

s = student("Female","Mumbai")
print(s.intro("Tia",16))
print("\n")  

p = prof("Male","Delhi")
print(p.intro("Mohan",55))
