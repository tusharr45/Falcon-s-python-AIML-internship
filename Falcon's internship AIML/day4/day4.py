# slicing and indexing 



s='poornima '
print(s[0:5])
# forward slicing


print(s[-5:-1])
print(s[-1:-5])
# backward slicing 



b= 'python program'
print(b[: :])

# reverse order
print(b[-1:])

print(b[:-1])

print(b[::-1])  # reverse order 

ans=s[: : -2]
print(ans)

print(b[1:10:-1])  #empty sring 

print(s[::])
print(s[::1])
print(s[::-1])

print(s[::-2]) # -2 backward gap

print(b[-5:-12:-1])
print(b[-15:-1])


print(b[3:-4])

   

a="/====================list=========================/"
print(a)


# list 
# list is mutable

l=[10,'string',1000,12.06]
print(l)
print(id(l))
print(type(l))

print(l[2])
print(l[3])

l[1]=999 # value change 



print(l)

print(id(l))

l1=[10,20,30]

print(l1)
print(id(l1))

l2=list(l1)   # for changing list location 

print(l2)
print(id(l2))



ll=[11,12,13,14,15]
print(ll[0 : 3])
print(ll[: 4 :-1])

print(ll[-20:4])

# nested list 

l0=[1,2,3,4,5,[100,200,]]
print(l0)
print(l0[5])


anss=l0[5][1]

print(len(l0))
print(l0.index(3))

# append

l0.append(9087)                     # for single value append 
l0.extend(["one","thw","thre"])     # for multiple value append 
l0.insert(1,'i am string ')         #when we input in mid  
l0.pop()                            # this function do last value remove  

l0.remove('i am string ')           #it only remove specific value 
l0.clear()                          # It remove entire list 



l0.append(10)
l0.append(-100)
l0.append(45)
l0.append(19)




print(l0)
print(max(l0))
print(min(l0))
print(sum(l0))

# list sort / sorting

l0.sort()                       # it run in ascending order 
l0.sort(reverse=True)           # it run in decending
print(l0)



lix=[11,12,13,14]
lix.reverse
print(lix)
