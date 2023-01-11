#print prime
num = 5
for i in range(2,num+1):
	for j in range(2,i):
		if (i % j) == 0:
			break
	else:
		print(i)
#check prime
flag = False
if num == 1:
	print("Its not prime")
elif num > 1:
	for k in range(2,num):
			if (num % k) == 0:
				flag = True
				break
	if flag:
		print("Its not prime")
	else:
		print("Its a prime")





