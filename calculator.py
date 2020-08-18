

def calc(number1,number2,operation):
   if (number1.isnumeric() and number2.isnumeric())==True:
       if operation=='+':
           answer=int(number1)+int(number2)
           print("The answer is %d "%(answer))
       elif operation=='-':
           answer=int(number1)-int(number2)
           print("The answer is %d "%(answer))
       elif operation=='/':
           answer=int(number1)/int(number2)
           print("The answer is %d "%(answer))
       elif operation=='':
           answer=int(number1)*int(number2)
           print("The answer is %d "%(answer))
       else:
            print("operation is invalid")
   else:
       print("the entered numbers are invalid")
def main():

  number1=input("Enter the first number:")
  number2=input("Enter the second number: ")
  operation=input("Choose the operation (+, -, /, ): ")
  calc(number1,number2,operation)


if __name__ == '__main__':
	main()
