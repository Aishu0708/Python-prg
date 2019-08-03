n=int(input("Enter the number : "))
fact=1
if n<0:
  print("Factorial cannot be found.")
elif n==0:
    print("The factorial is 1.")
else:
    for i in range(1,n+1):
          fact=fact*i
print("The factorial of",n,"is",fact)
