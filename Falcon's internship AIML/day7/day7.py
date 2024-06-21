# nested for loop (loop ineer  loop)

'''==========================================================[Pattern with *]==============================================='''
a=5

for i in range (1,6):     #rows
       print("row is : " ,i)
for j in range(1,6):    #columns 
       
            print("*",end="")
            print("\a")
       



'''==========================================================[Pattern ]==============================================='''

n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
        print("\n")


'''==========================================================[Pattern with ascii]==============================================='''


n=5
for i in range(1,n+1):
    for j in range(1,n+1):

        asc=ord('A')
        ch=chr(asc+ i-1)
        print(ch,end="")
        print("\n") 




'''==========================================================[function]==============================================='''

def one():
    print("i am one function")
 
def fun(one):
    a,b,c,d=11,12 ,13,14
    
    return a,b,c,d
    
    print(one)
    one()



    
