#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the #array. The array can contain duplicates and negative numbers as well. For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
print("Enter a list of integers that can include postive and negative values incremented by 1 with atleast one postive missing postive ")
a=[int(x) for x in input().split()]
a.sort()
b=[]
x1=0
for i in a:
	if i not in b and i>=0:
		b.append(i)
print(b)
for j in range(b[0], len(b)+1):
	if x1==len(b)-1:
		print("All values are in order, nothing missing")
		break
	elif (b[x1]-j>0):
		print("The first missing number is", j)
		break 
	else:
		x1=x1+1
		continue
print(x1)






		


	