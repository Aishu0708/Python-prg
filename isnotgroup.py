def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
a=input("Enter a group : ")
b=input("Enter a group member : ")
print(is_group_member(a,b))
