print ("Welcome to Calculator!")
#after Welcoming we set out basic math functions and initialize the res variable
res = 0 
def sum(x,y): return x + y

def less(x,y): return x - y

def times(x,y): return x * y

def divided(x,y): return x / y
# In order to make a loop calculator as a actual software we use a while True
while True:
#begging the while setting the variables which should be reseted every loop
    num1 = 0
    num2 = 0

#ask for the desired operation to user
    
    operation = str(input("\n Type +, -, *, /  or 1 to stop \n"))

    #if that stops the software so this is not a infinity loop
    if operation == "1":
        break
        print ("\n Thank you for using my software, Goodbye!")

    elif operation != "+" and operation != "-" and operation != "/" and operation != "*":
        print ("\nInvalid operation")
        continue


#asking for the nubers which will be operated
    num1 = float(input("\n Give me the firt number of the operation: \n"))
    num2 = float(input("\n Give me the second number of the operation: \n"))

    if operation == "+":
        res=sum(num1,num2)

    elif operation == "-":
        res=less(num1,num2)

    elif operation == "*":
        res=times(num1,num2)

    elif operation == "/":
        if num2 and num1 != 0:
            res=divided(num1,num2)
        else:
            print("\n Not possible to divide 0 ou divide something by 0")
            continue 

    print ("\n Result: \n",res)
