

arr = [6,8,3,8,4]

num = int(input("How many elements you want to add:- "))

for i in range(num):
    arr.append(int(input("Enter "+str(i+1)+"_element to add:- ")))


for i in arr:
    print(i)