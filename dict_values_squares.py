def squares(n):
	ans = {}
	for i in range(1, n + 1):
		ans[i] = i * i
	return ans
a=int(input("Enter the number  : "))
print("The dictionary values are : ",squares(a))
