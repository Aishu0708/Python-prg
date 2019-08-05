def test_number(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
     else:
         return False
a=int(input("Enter x : "))
b=int(input("Enter y : "))
print(test_number(a,b))
