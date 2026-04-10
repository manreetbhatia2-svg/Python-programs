#Calculator program
import math
print ("What operation do you want to perform?\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Log\n6.Trigonometry\n" )
option = int(input("Enter the option "))

match option:
    case 1: # add
        num1 = int(input("Enter the 1st number "))
        num2 = int(input("Enter the 2nd number "))
        print("Sum = ",num1+num2)
    case 2:  #subtract
        num1 = int(input("Enter the 1st number "))
        num2 = int(input("Enter the 2nd number "))
        print("Difference = ",num1-num2)
    case 3:  #multiply
        num1 = int(input("Enter the 1st number "))
        num2 = int(input("Enter the 2nd number "))
        print("Product = ",num1*num2)
    case 4:  # divide
        num1 = int(input("Enter the 1st number "))
        num2 = int(input("Enter the 2nd number "))
        print("Quotient = ", num1/num2)
    case 5:  #log
        num = int(input("Enter the number "))
        base = int(input("Enter the base "))
        print("Result = ",math.log(num,base))
    case 6:  # trigonometry
        take_angle = int(input("Enter the angle in degrees "))
        operator = int(input("Which trigonometric operation do you want to perfrom\n1.sin\n2.cos\n3.tan "))
        match operator:
            case 1:
                print(f"sin {take_angle}deg = ",math.sin(math.radians(take_angle))) 
            case 2:
                print(f"cos {take_angle}deg = ",math.cos(math.radians(take_angle)))
            case 3:
                print(f"tan {take_angle}deg = ",math.tan(math.radians(take_angle)))
