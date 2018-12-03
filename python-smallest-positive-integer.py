A = [-1,2,3]
testMap=dict()
for ele in A:
	testMap[ele]=1

flag = 0
i=1
while flag==0:
	if i in testMap:
		i+=1
	else:
		flag=1
		print i
