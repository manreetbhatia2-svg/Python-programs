class Students:
    def __init__(self,roll_num):
        self.roll_num = roll_numś
        marks1 = int(input("Enter marks for Physics "))
        marks2 = int(input("Enter marks for Math "))
        marks3 = int(input("Enter marks for Chemistry "))
        print(f"\nRoll number {roll_num}\nTotal marks scored = {marks1 + marks2 + marks3}/300\nPercentage marks= {(marks1 + marks2 + marks3)/3:.2f} %")

print("For roll number 20") 
student1 = Students(20)
print("\nFor roll number 33") 
student2 = Students(33)

