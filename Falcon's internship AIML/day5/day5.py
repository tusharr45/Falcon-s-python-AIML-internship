
l=[10,9,-10,89,23]

l.sort()
print(l)


l.sort(reverse=True)                   #It effect on original list
print(l)    

ans=sorted(l)                          #It does not effect on original list
x=sorted(l,reverse=True)
print(ans)
print(l)

print(x)
print(l)

l1=[1,2,3,'name']
l2=[10,20,30]

anss=l1+l2

print(anss)

nn=l1*3
print(nn)




# Tuples 
t=(1,2,3,4,5,'string')
print(t)
print(type(t))


# for multiple value assigning

a,b,c=10,20,30.5
print(a)
print(b)
print(c)

aa=1,2,3,4   
print(aa)
print(type(aa))


tt=(1,2,3)
print(tt)


print(len(tt))


(aa,bb,cc)=tt
print(aa)
print(bb)
print(cc)


Y=10
Yb='i am sring'
YY=20

O=(Y,Yb,YY)
print(O)




# slicing in tuples

q=(5,6,7,8,9)
# qq=q[0:-2]
# qq=q[-1:-20:1]    #empty tuples
print(q)

print(len(q))

print(q.count(8))

print(q.index(8))



# isme sort function apply nahi hoga


# islie use karenge sorted 
w=(100,5,6,-20,7,50,8,9,8)
aaa=sorted(w)
print(aaa)

print(sorted(aaa,reverse=True))  #decending order 

# del It delete whole tuple 
print(w)

print(min(w))
print(max(w))

e=w*3
print(e)

# two tuples adding 

w1=(100,5,6,-20,7,50,8,9,8)
w2=('10','20','30')
w2=w1+w2
ww=w2+w1
print(ww)
print(w1+w2)
print(w2)



# set

a=[]

b=()

c={}
cc={1,2,3,3,2,1,1,1}
print(type(a))
print(type(b))
print(type(c))
print(type(cc))
print(cc)

cc.add(2)
cc.add(34)
cc.add('set')

# cc[0:]   not able to perform indexing 
# print(cc[0])


print(len(cc))
cc.remove(3)

# cc.remove(999)             # when he "999" isnot conain then we have a error
cc.discard('set')
cc.discard(999)              # It does not have an error either it contain or not "999"
print(cc)



s1={1,2,3,3,2,1,1,1,'name',1000}

s2={11,22,33}
# s1.update(s2)
s2.update(s1)

# s1=s1+s2 this is not support set 
print(s1)




ss1={10,20,30,40}
ss2={20,40,50,60}

a22=ss1.union(ss2)
print(a22)

sd=ss1.intersection(ss2)
print(sd)

sdd=ss1.difference(ss2)
print(sdd)

sddd=ss2.difference(ss1)
# sddd=ss2-ss1
print(sddd)

sa=ss1.symmetric_difference(ss2)
print(sa)


# in se pop remove any value 
print(ss1.pop())
print(ss2.pop())

ss11={1,2,3}
ss22={3,2,1}
print(min(ss11))
print(max(ss22))

print(ss11==ss22)