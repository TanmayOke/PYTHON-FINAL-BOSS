list_1=[1,2,3,4,5,["Ram","Hero","Ankit"]]
print(list_1)
print(list_1[5])
print(list_1[5][2])

list_1.pop()
print(list_1)

list2=[1.0,2.0,3.0,6.0,4.,5.0]
list0fNmaes=["Tanmay","Rahul","Mohan","Somesh"]

list2.sort()
print(list2)

len(list0fNmaes)

print("The avaearge of list2 is:-",sum(list2)/len(list2))

for i in list0fNmaes:
    print(i)

print(type(list0fNmaes),type(list2))    
print(type(list0fNmaes[0]),type(list2[3]))  

#slicing of lists
new_list=list2[0:3]
print(new_list)
new_list[3:8]=[5,6,7,8,9]
print(new_list)
print(max(new_list))