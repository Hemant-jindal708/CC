import random
# question1
l=[10,20,30,40,50,60,70,80]
print("original list",l)
l.append(200)
l.append(300)
print("200,300 add to list",l)
l.remove(10)
l.remove(30)
print("10,30 removed",l)
l.sort()
print ("sorted list (ascending)",l)
l.sort(reverse=True)
print ("sorted list (descending)",l)


#question 2
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
max = max(scores)
index=scores.index(max)
print ("max element in tuple ",scores," is ",max," at index ",index)
min = min(scores)
count=scores.count(min)
print ("min element in tuple ",scores," is ",min," with count ",count)
print (tuple(reversed(scores)))
if(76 in scores):
    print("element 76 is present with no. of counts ",scores.count(76))
else:
    print("element not found")

#question 3
l=[]
even=[]
odd=[]
prime=[]
for i in range(5):
    l.append(random.randint(100,900))
for a in l:
    if a%2==0:
        even.append(a)
        
    else:
        odd.append(a)
print ("list generated ",l)
print ("all even number generated" ,even)
print ("all odd no. generated ",odd)

#question 4
A = {34, 56, 78, 90} 
B = {78, 45, 90, 23}
print ("union of sets ", set.union(A,B))
print ("intersection of sets ", set.intersection(A,B))
print ("exclusive score for A",A-B)
print ("exclusive for B",B-A)
print (set.issubset(A,B))
print (set.issuperset(B,A))
x=int(input("eneter element:"))
if x in A:
    set.remove(A,x)
    print ("new scores for team A ",A)
else:
    print("score not found")

#question 5
direc={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"new york"
}
direc["location"]=direc.pop("city")
print(direc)