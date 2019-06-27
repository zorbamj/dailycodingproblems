#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

import random

def sucproduct(a,x):
	s=1
	if (x!=n-1):
		for i in range(x,n-1):
			s*=a[i+1]
	return s

def preproduct(a,x):
	s=1
	if (x>0 and x <n):
		for i in range(0,x):
			s*=a[i]
	return s

while True:
	try: 
		n=int(input("Please enter the length of list you want to be generated "))
	except ValueError:
		print("Sorry, I can accept only numbers")
		continue
	if (n<2):
		print("A list should be atleast of length 2")
	else:
		break 

while True:
	try:
		l_min=int(input("Enter the lower limit of the list "))
	except ValueError:
		print("Sorry please enter a number")
		continue
	else:
		break


while True:
	try: 
		l_max=int(input("Enter the upper limit of the list "))
	except ValueError:
		print("Sorry please enter a number")
		continue
	if (l_max<=l_min):
		print("Upper limit cannot be lesser than or equal to lower limit. Please enter a higher value ")
	else:
		break

gen_list=[]
prod_list1=[1 for i in range(n)]
prod_list2=[1 for i in range(n)]

for i in range(n):
	gen_list.append(random.randint(l_min,l_max))

for i in range(n):
	prod_list1[i]=sucproduct(gen_list,i)
	prod_list2[i]=preproduct(gen_list,i)*prod_list1[i]

print("The input list is ", gen_list)
print("The desired list is ", prod_list2)