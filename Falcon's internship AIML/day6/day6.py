dic = {
'name' : "shreyansh",
'city': "jaipur",
'edu' : "cs",
'number' : 123,
}


print(dic)

# dic['name]-'shre'
# print(dic)


# dic['python']='language'
# print(dic)

# dic['python']='aiml'
# print(dic)


'''==========================================================[update function]==============================================='''


dic2 = {1: "one", 2 : "two"}

dic.update(dic2)
print(dic)

# when we want dic2 value first 

dic2.update(dic)
print(dic2)


#   when we want delete specific value  

dic['k']=123
# want to value add 

del dic['number']
print(dic)


#when we want delete specific key value 

dic.pop('k')
print(dic)


dic.popitem()                  # only delete last item 
print(dic)

 
# dic.clear()                  # it's delete whole diciionary
# print(dic)

print(len(dic))                # To find dicionary lenth

print(dic.items())             # when we show dicionary to tuple
print(dic.keys())              # it shows key 

print(dic.values())            # it only show values  



dicc1={
    1:10,
    2:100,
    3:-1000,
    4:99999
}

print(min(dicc1))

print(max(dicc1))