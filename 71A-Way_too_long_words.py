n = int(input())
for i in range(n):
  x = input()
  if len(x) > 10:
    print(x[0] + str(len(x)-2) + x[-1])
  else:
    print(x)
