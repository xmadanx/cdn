list = [9,8,10,1,2,3,4,5,6,7]
s = 0
for i in range(0,len(list)):
	s = list[i] + s
print(s)
#builtin function
s1 = sum(list)
print(s1)
#largest and smallest
print(max(list))
print(min(list))

list.sort()
print(list[-1])
#largest 2nd number
print(list[-2])
#smallest 2nd number
print(list[1])
