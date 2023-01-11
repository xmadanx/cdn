x = [[1,2,1],
	 [2,1,3],
	 [4,3,2]]
y = [[1,1,1],
	 [1,1,1],
	 [1,1,1]]
r = [[0,0,0],
	 [0,0,0],
	 [0,0,0]]

for i in range(len(x)):
	for j in range(len(x[0])):
		r[i][j] = x[i][j] + y[i][j]
for k in r:
	print(k)