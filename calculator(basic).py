# define function needed, add,sub, nul, div...
# print options to the user 
# get user input ( add, sub , nul, div)
# call the functions
# while loop to continue the program until user want to exit
# define function needed, add,sub, nul, div...
# print options to the user 
# get user input ( add, sub , nul, div ...)
# call the functions
# while loop to continue the program until user want to exit


        
import math
import sys
def add(a,b):
    toplama = a+b
    
    return str(a) + "+" + str(b) + "=" + str(toplama)
def sub(a,b):
    cıkartma = a-b
    return str(a) + "-" + str(b) + "=" + str(cıkartma)
def nul(a,b):
    carpma = a*b
    return str(a) + "*" + str(b) + "=" + str(carpma)
def div(a,b):
    bolme = a/b
    return str(a) + "/" + str(b)+ "=" + str(bolme)
def square(a):
    carpma = a*a
    return str(a) + "^" + str(2) + " = " + str(carpma) 
def kalan(a,b):
    yüzde = a%b
    return str(a) + "%" + str(b) + "=" + str(yüzde)
def tan():
   tan1 = float(input("enter number: "))
   return "tan : " + str(math.tan(tan1))
def sin():
    sin1 = float(input("enter number: "))
    return "sin : " + str(math.sin(sin1))
def cos():
    cos1 = float(input("enter number: "))
    return "cos : " + str(math.cos(cos1))
def log():
    log1 = float(input("enter number: "))
    return "log : " + str(math.log(log1))

while True:
    choice =str(input("What is your choice ? \n1.add + \n2.sub - \n3.nul * \n4.div / \n5.square ** \n6.% \n7.exit\n")).lower()
           
    if choice == "add"  or choice == "1":  
        value1= int(input("enter a value : "))
        value2= int(input("enter a value : "))      
        result = add(value1,value2)
        print(result)    
    elif choice == "sub" or choice == "2":
        value1= int(input("enter a value : "))
        value2= int(input("enter a value : "))  
        result = sub(value1,value2)  
        print(result)  
    elif choice == "nul"  or choice=="3":
        value1= int(input("enter a value : "))
        value2= int(input("enter a value : "))  
        result =nul(value1,value2)
        print(result)    
    elif choice == "div"  or choice=="4":
        value1= int(input("enter a value : "))
        value2= int(input("enter a value : "))  
        result =div(value1,value2)
        print(result) 
    elif choice == "square" or choice == "sqr" or choice == "5":
        value1= int(input("enter a value : "))
        result =square(value1)
        print(result) 
    elif choice == "%" or choice == "6":
        value1= int(input("enter a value : "))
        value2= int(input("enter a value : "))  
        result = kalan(value1,value2)
        print(result)
    elif choice == "tan" or choice =="7":
        result =tan()
        print(result)
    elif choice == "sin" or choice =="8":
        result =sin()
        print(result)
    elif choice == "cos" or choice =="9":
        result =tan()
        print(result)
    elif choice == "log" or choice =="10":
        result =log()
        print(result) 
    elif choice =="exit" or choice == "Exit" or choice == "E" or choice =="11":
        sys.exit(0)
        #exit()
