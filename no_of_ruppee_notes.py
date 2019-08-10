def no_notes(a):
  Q = [2000,1000,500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(8):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
b=int(input("Enter the number : "))
print("The number of notes for the given number",no_notes(b))
