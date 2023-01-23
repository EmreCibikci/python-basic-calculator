# define function needed, add,sub, nul, div
# print options to the user 
# get user input ( add, sub , nul, div)
# call the functions
# while loop to continue the program until user want to exit
def add(a,b):
    toplama = a+b
    print(str(a) + "+" + str(b) + "=" + str(toplama))
def sub(a,b):
    cıkartma = a-b
    print(str(a) + "-" + str(b) + "=" + str(cıkartma))
def nul(a,b):
    carpma = a*b
    print(str(a) + "*" + str(b) + "=" + str(carpma))
def div(a,b):
    bolme = a/b
    print(str(a) + "/" + str(b)+ "=" + str(bolme))
    
def exponentiation(a,b):
    carpma = a*b
    print(str(a) + "^" + str(a) + " = " + str(carpma) )
def kalan(a, b):
    yüzde = a%b
    print(str(a) + "%" + str(b) + "=" + str(yüzde))
    
while True:
    choice =str(input("What is your choice ? \n1.add + \n2.sub - \n3.nul * \n4.div / \n5.square \n6.%\n7.exit\n")).lower()
    if choice =="exit" or choice == "Exit" or choice == "E" or choice =="7":
        exit()
          
    value1= int(input("enter a value : "))
    if choice == "square"   or choice == "sqr" or choice == "5":
            print(exponentiation(value1))
    value2= int(input("enter a value : "))

        
    if choice == "add"  or choice == "1":        
            print(add(value1,value2))      
    elif choice == "sub"   or choice == "2":
            print(sub(value1,value2))     
    elif choice == "nul"  or choice=="3":
            print(nul(value1,value2))    
    elif choice == "div"  or choice=="4":
            print(div(value1,value2))
    elif choice == "%" or choice == "6":
            print(kalan(value1,value2))