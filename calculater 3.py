print("What would you like to do?")
#displaying the question
print("1=Add\n2=subtract\n3=divide\n4=Multiply")
#Displaying four different options to choose the right calculation.
choice=int(input())
#Getting user's input ans saving it as an integer.

print("Please enter 7 numbers")
n1=float (input())
n2=float (input())
n3=float (input())
n4=float (input())
n5=float (input())
n6=float (input())
n7=float (input())
#Getting the seven number from the calculations.

if choice==1:
    #if the user chooses 1 then:
    answer=n1+n2+n3+n3+n4+n5+n6+n7
    #the value of answer is calculated by adding two numbers

elif choice==2:
    #if the user chooses choice 2 then:
    answer=n1-n2-n3-n4-n5-n6-n7

elif choice==3:
    answer=n1/n2/n3/n4/n5/n6/n7
    
else:
    #if any other number is entered here then:
    answer=n1*n2*n3*n4*n5*n6*n7

print(answer)





    
