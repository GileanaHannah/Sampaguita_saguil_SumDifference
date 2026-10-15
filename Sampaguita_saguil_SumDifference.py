#AUTHOR: Gileana Hannah G. Saguil
# October 15, 2026
#Hands-on Activity Sum nand difference Calculator

#ask for the user's input (numbers)
print("Note that the digit that will be shown first is the sum after it is calculated.")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

def calculate_sum():
    global num1, num2 #This is a global variable
    sum = num1 + num2 #This is a local variable
    print(sum)
calculate_sum() #display the sum

def calculate_difference():
    global num1, num2
    difference = num1 - num2
    print(difference)
calculate_difference() #display the difference






