n,k=map(int,input().split(' '))
score = list(map(int, input().split(' ')))
 
total=0
for point in score:
    if point!=0 and point>=score[k-1]:
        total+=1
print(total)
