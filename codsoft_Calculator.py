
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


while True:
    print("Please select the operation You want to perform from (1-4):\n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
 
    ch=int(input("Enter your choice: "))
    if ch in (1,2,3,4):
        try:
         num1=int(input("Enter first number:"))
         num2=int(input("Enter second number:"))
        except ValueError:
         print("Please enter valid number")
         continue

        if ch==1:
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif ch==2:
            print(f"{num1}-{num2}={sub(num1,num2)}")
        elif ch==3:
            print(f"{num1}*{num2}={mul(num1,num2)}")
        elif ch==4:
            print(f"{num1}/{num2}={div(num1,num2)}")

        next_op=input("Do you want to continue...(yes/no):")
        if next_op=="no" or next_op=="No":
            break

    else:
      print("invalid Choice..........")

