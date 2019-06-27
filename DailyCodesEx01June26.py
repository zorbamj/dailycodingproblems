#Given a list of numbers and a number k, return whether #any two numbers from the list add up to k.For example, #given [10, 15, 3, 7] and k of 17, return true since 10 #+7 is 17.Bonus: Can you do this in one pass?.

import random

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
		print("How can upper limit lesser than or equal to lower limit, please enter a higher value ")
	else:
		break

while True:
	try: 
		user_entry=int(input("Enter sum to be checked "))
	except ValueError:
		print("Sorry, I can accept only numbers")
		continue
	if (user_entry>=(2*l_max) and user_entry<l_min):
		print("Case is impossible, the sum cannot go beyond twice the upperlimit and below lower limit")
	else:
		break

gen_list=[]
check_list=[]

for i in range(n):
	gen_list.append(random.randint(l_min,l_max))

print(gen_list)
for j in gen_list:
	if (user_entry-j) in check_list:
		print("The below pair exists in the generated list whose sum is equal to ",user_entry)
		print((user_entry-j),j)
		break
	else:
		check_list.append(j)

if (gen_list==check_list):
	print("Pairs do not exist")
	print(check_list)

