# ===============================matplotlib===============================#

import numpy as np
from matplotlib import pyplot as plt

x=np.array([1,2,3,4,5])
y= 2*x

x=[1,2,3,4,5]
y=[11,12,13,14,15]

plt.plot(x,y)
plt.plot(x,y,color="yellow",linewidth="2",linestyle=":")

plt.xlabel("x axis")
plt.ylabel("y axis")

plt.title("line chart")
plt.show()

# line plot
a=np.arange(11,20)
y1=2*x
y2=3*x
plt.plot(x,y1,color="green",linestyle=":",linewidth="3")
plt.plot(x,y2,color="green",linewidth="3",linestyle=":")
plt.grid(True)
plt.show()




'''
import numpy as np
from matplotlib import pyplot as plt

x=np.array([1,2,3,4,5])
y=2*x


# x= =[1 ,2,3, 4,5 ]   ==> indepent variable
# y=[2, 4 ,6 , 8 , 10]===> dependent veriable


#plt.plot(x,y)
plt.plot(x,y,color="yellow", linewidth="2", linestyle=":")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line chart")
plt.show()
'''
# line plot

x=np.arange(11,20)

#x=[11 12, 13 ,14 ,15 ,16 , 17 , 18 ,19]
y1=2*x
y2=3*x
plt.plot(x,y1,color="green" ,linestyle=":",linewidth="2")
plt.plot(x,y2,color="red" ,linestyle="-",linewidth="2")
plt.grid(True)
plt.show()


# line subplot
plt.subplot(1,2,1)
plt.plot(x,y1,color="green" ,linestyle=":",linewidth="2")
plt.subplot(1,2,2)
plt.plot(x,y2,color="red" ,linestyle="-",linewidth="2")
plt.show()


# bar ,plot is used when there is categotical data

student={"aayush":60,"sheyansh":80,"jain":50}
print(type(student))

# print(type(student.keys() ))
# print(type(student.values()))

# print(type(student.items()))

name=list(student.keys())

# name=['aayush' , 'shreyansh' ,'jain']
#value =[60,80,50]

marks=list(student.values())
# print(type(name))
# print(type(marks))

plt.bar(name,marks)
plt.title("bar chart")
plt.xlabel(" name ")
plt.ylabel(" marks ")
plt.grid(True)
plt.show()

#  horizental bar ,plot is used when there is categotical data

student={"a":60,"b":80,"c":50}
name=list(student.keys())
marks=list(student.values())
print(name)
print(marks)

plt.barh(name,marks, color="green")
plt.title("horizontal bar chart")
plt.xlabel(" marks ")
plt.ylabel(" name ")
plt.grid(True)
plt.show()

# scatter plot==> find out the distribution between two numerical entitiy which is of same entity

# a=np.random.randint(20,31,10)   # x asis
# b=np.random.randint(1,11,10)     # y axis

a=[10,13,90,67,89]
b=[20,78,45,12 ,70]

plt.scatter(a,b)
plt.show()


# scatter with marker
a=np.random.randint(20,31,10)
b=np.random.randint(1,11,10)
plt.scatter(a,b, marker="*" , color="pink" ,s=100)
plt.show()


# scatter subplot

p=np.random.randint(40,51,10)   #x
q1=np.random.randint(10,21,10)  #y1
q2=np.random.randint(20,31,10)   #y2

plt.scatter(p,q1 , color="red")
plt.scatter(p,q2,marker="*" ,color="green",s=100)
plt.show()


# sub scatter plot


p=np.random.randint(40,51,10)
q1=np.random.randint(10,21,10)
q2=np.random.randint(20,31,10)

plt.subplot(1,2,1)
plt.title("sub scatter plot 1")
plt.scatter(p,q1 , color="red")
plt.subplot(1,2,2)
plt.title("sub scatter plot 2")
plt.scatter(p,q2,marker="*" ,color="green",s=100)
plt.show()

# histogram
x=[1,2,3,3,3,2,6,6,6,6,6,7,8,8,9,9,9]

plt.hist(x)
plt.show()

print("\n\n")

# historgram with limited bins
plt.hist(x ,color="pink" ,bins=4)
plt.show()

# box plot ==> gives 5 number summery of numerical columns as a list [ min , 25 % , 50 % , 75% , max ]

one=[10,20,30,40,50]
two=[51,55,57,59,70,80]
three=[40,32,20,45,75,95]
data=list([one,two,three])

plt.boxplot(data)
plt.show()

# box plot ==> gives 5 number summery of numerical columns as a list [ min , 25 % , 50 % , 75% , max ]

one=[10,20,30,40,50]
two=[51,55,57,59,70,80]
three=[40,32,20,45,75,95]
data=list([one,two,three])

plt.boxplot(data)
plt.show()

# vilonplot is similar as a box plot
one=[10,20,30,40,50]
two=[51,55,57,59,70,80]
three=[40,32,20,45,75,95]
data=list([one,two,three])

plt.violinplot(data ,showmedians=True)
plt.show()


# piechart => it help to understand the frequency of different categorical value

fruits=['mango','lichi','watermalon','pinaple']   # x asix
persantage=[70 ,50, 90 , 60]   # y asix

#plt.pie(persantage, labels=fruits)
plt.pie(persantage, labels=fruits,autopct='%0.1f%%')
plt.show()
