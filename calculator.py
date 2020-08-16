
def main():
      number1 = input(" Enter the first number :  ")
      n1 = int(number1)
      number2 = input(" Enter the second number : ")
      n2 = int(number2)
      operation = input(" Choose the operation (+, -, /, *) : ")
      answer = 0
      if operation == "+":
        answer =  n1+n2
      elif operation == "-":
        answer = n1-n2
      elif operation == "/":
        answer = n1/n2
      elif operation == "*":
        answer = n1*n2
      print("The answer is " + str(answer))



if __name__ == '__main__':
	main()
