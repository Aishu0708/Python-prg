str1 = input("Enter the string : ")
sub =input("Enter the substring : ")
count = 0
index = 0
for i in range(0, len(st)):
    if st[i] == sub[0]:
        if st[i:i+len(sub)] == sub:
            count += 1
print count
