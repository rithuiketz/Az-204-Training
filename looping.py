li = [0,1,2,3,4] 

for i in li:
    print(i)
print("&&&&&&&&&&&&&&&&&&&&&")
for i in range(0,len(li)):
    print(li[i])
print("&&&&&&&&&&&&&&&&&&&&&")
cnt =0 
while cnt < len(li):
    print(li[cnt])
    cnt+=1

li  = [x for x in li if x%2==0]

print(li)