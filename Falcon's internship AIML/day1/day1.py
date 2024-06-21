# Python 

print("Hello world")  #first program of print function 

# Data types 
# 1. string  = "A to Z ", " anything "
# 2. int  = decimal Base(0 to  9), binary Base (0 or 1 ), ocatl Base (o to 8 ), hexadecimal Base (0x101)(0 to 16) 
# 3. Boolean = True, False 
# 4. Float= 12.5,2.5,33.2,
# 5. complex

# how to convert datatypes
# binary to int
        
            #   '''  0   1   0    1  1   0
            #    2^5 2^4 2^3 2^2 2^1 2^0

            #    0+2+4+0+16+0=22
            #    '''
# binary 
c= 0b111
print(type(c))
print(c)

# octal

o= 0o011
print(o)

        #   0             1             1
        #    8^2              8^1             8^0
        #    0                 8               1    = 9

# hexadecimal
hex=0x101
print(hex) 

# decmal (base10)
d=100
print(d)


a= 10     # [a is varibale ] and [ 10 is value ] variable storing data 

print(a)

print(type(a))



# fractional part

floatx=1233.83
print(floatx)
print(type(floatx))

f=1.2e3
# 1.2 * 10^3 
print(f)

# complex

ll=5+6j
print(type(ll))
print(ll.real)
print(ll.imag)


x=12
z=13
print(x+z)


i=6+3j
ii=3+5j
print(i+ii)






# Boolean(True or Fasle)
bl= True

print(bl)
print(type(bl))


bll=False
print(type(bll))
print(bll)

blll= 4*True
print(blll)



bllll=4*False
print(bllll)
